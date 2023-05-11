# import
import gurobipy as gb
from gurobipy import GRB
import sys
import time
from MIP_train_timetable_problem import mip_input_parser


class MIPModel:
    # operating_mode: 0 = solve problem for new train, 1 = solve timetable finding problem for existing trains (useful
    #   when generating network data)
    # mip_mode: 0 = mip decides all variables, 1 = existing trains timetables are fixed
    # print_solution: 0 = zero output, 1 = only gurobi output, 2 = gurobi and solution output
    # can only work with parsed data
    def __init__(self, parsed_data: dict, filepath: str = None, operating_mode: int = 0,
                 mip_mode: int = 0, print_solution: int = 0):
        # only continue if filepath xor input_data is given as input
        self.filepath = filepath
        self.input_data = parsed_data
        self.operating_mode = operating_mode
        self.mip_mode = mip_mode
        self.print_solution = print_solution
        self.model = None
        self.model_status = 0  # 0 => infeasible, 1 => solved/feasible
        self.variable_references = None
        self.time_dict = {'mip_creation_time': 0.0, 'mip_solving_time': 0.0, 'mip_execution_time': 0.0}
        self.resulting_timetable = None

    def execute_full_model(self):
        self.construct_model()
        self.solve_model()
        self.get_solution_of_model()

    def construct_model(self):
        start_time = time.time()

        # train data
        R1 = self.input_data['trains'].copy()
        R1.append(9991)  # artificial first ...
        R2 = self.input_data['trains'].copy()
        R2.append(9999)  # ... and last train
        T = range(self.input_data['timehorizon'])  # time in minutes

        O = {}  # stops for each train
        for r in self.input_data['trains']:
            O[r] = self.input_data['stations']

        AS = set()  # actual stops
        for s in self.input_data['stations']:
            for b in self.input_data['station_blocks'][s]:
                AS.add(b)

        # model
        model = gb.Model('ttp')

        # params
        if not self.print_solution:
            model.setParam('OutputFlag', 0)
        model.setParam('Timelimit', 300)

        # variables
        u = model.addVars(self.input_data['trains'], list(self.input_data['blocks']), vtype=GRB.BINARY,
                          name='u')  # use block b or not
        a = model.addVars(self.input_data['trains'], list(self.input_data['blocks']), vtype=GRB.INTEGER, lb=0,
                          name='a')  # arrival time for block b
        d = model.addVars(self.input_data['trains'], list(self.input_data['blocks']), vtype=GRB.INTEGER, lb=0,
                          name='d')  # departure time for block b
        x = model.addVars(R1, R2, list(self.input_data['blocks']), vtype=GRB.BINARY,
                          name='x')  # train r2 directly follows train r1 on block b
        if not self.operating_mode:
            # relaxing arrival variables (violating arrival constraints)
            y = model.addVars(self.input_data['trains'], AS, vtype=GRB.INTEGER, lb=0, name='y')
            # relaxing arrival variables (violating arrival constraints)
            z = model.addVars(self.input_data['trains'], AS, vtype=GRB.INTEGER, lb=0, name='z')
            # time constraint for last block, enforcing that the train travels full distance
            """m = model.addVar(vtype=GRB.INTEGER, lb=0)"""
            m = model.addVars(self.input_data['trains'], vtype=GRB.INTEGER, lb=0, name='m')
        elif self.operating_mode:
            # minimize the time the trains need to pass the network
            m = model.addVars(self.input_data['trains'], vtype=GRB.INTEGER, lb=0, name='m')
            model.setParam("MIPFocus", 1);

        # save references of variables in dictionary to make reading of the output easier later on
        if not self.operating_mode:
            self.variable_references = {'u': u, 'a': a, 'd': d, 'x': x, 'm': m, 'y': y, 'z': z}
        else:
            self.variable_references = {'u': u, 'a': a, 'd': d, 'x': x, 'm': m}

        model.update()

        # set initial values for variables when checking timetable feasibility:
        if self.operating_mode:
            for r in self.input_data['trains']:
                time_counter = self.input_data['existing_trains'][r]['start']
                for l in self.input_data['layers']:
                    b = l[0]
                    a[r, b].VarHintVal = time_counter
                    time_counter += self.input_data['minimum_traveltimes'][(r, b)]
                    d[r, b].VarHintVal = time_counter
                    u[r, b].VarHintVal = 1

        # objective
        if self.operating_mode == 0:
            model.setObjective(sum(m[r] for r in self.input_data['trains'])
                               + sum(y[r, b] + z[r, b] for r in (self.input_data['trains']) for b in AS))
        elif self.operating_mode == 1:
            model.setObjective(sum(m[r] for r in (self.input_data['trains'])))

        # constraints
        # constraint 1: departure time is arrival time in the next block
        for r in self.input_data['trains']:
            for i in range(len(self.input_data['layers']) - 1):
                model.addConstr(
                    sum(d[r, b] for b in self.input_data['layers'][i]) == sum(
                        a[r, bb] for bb in self.input_data['layers'][i + 1]),
                    name="1a=d" + '_' + str(r) + '_' + str(i))

        # constraint 2: time spent on block is at least M_rb
        for r in self.input_data['trains']:
            for b in list(self.input_data['blocks']):
                model.addConstr(a[r, b] + self.input_data['minimum_traveltimes'][r, b] * u[r, b] <= d[r, b],
                                name="2timespent" + '_' + str(r) + '_' + str(b))

        # constraint 3: variable linking of a, d and u
        for r in self.input_data['trains']:
            for b in list(self.input_data['blocks']):
                model.addConstr(a[r, b] <= u[r, b] * self.input_data['timehorizon'],
                                name="3linking a and u" + '_' + str(r) + '_' + str(b))
                model.addConstr(d[r, b] <= u[r, b] * self.input_data['timehorizon'],
                                name="3linking d and u" + '_' + str(r) + '_' + str(b))

        # constraint 4: enforce visiting of train stations
        for r in self.input_data['trains']:
            for s in O[r]:
                model.addConstr(sum(u[r, b] for b in self.input_data['station_blocks'][s]) == 1,
                                name='4visiting' + '_' + str(r) + '_' + str(s))

        # constraint 5: flow conservation
        for r in self.input_data['trains']:
            for b in list(self.input_data['blocks']):
                if b != self.input_data['end_node']:
                    model.addConstr(
                        u[r, b] <= sum(u[r, bb] for bb in (list(self.input_data['blocks'])) if
                                       (b, bb) in self.input_data['edges']),
                        name='5flowconservation' + '_' + str(r) + '_' + str(b))

        # constraint 6: arrival constraints
        if self.operating_mode == 0:
            for r in self.input_data['trains']:
                # add arrival constraint for last block for all trains
                model.addConstr(a[r, self.input_data['end_node']] <=
                                self.input_data['arrival_times'][r, self.input_data['end_node']] + m[r],
                                name='6arrival_lastblock' + '_' + str(r))
            for r in self.input_data['existing_trains'].keys():
                for s in O[r]:
                    for b in self.input_data['station_blocks'][s]:
                        model.addConstr(a[r, b] <= self.input_data['arrival_times'][r, b] * u[r, b] + y[r, b],
                                        name='6arrival' + '_' + str(r) + '_' + str(s) + '_' + str(b))
        elif self.operating_mode == 1:
            for r in self.input_data['trains']:
                # link objective
                model.addConstr(a[r, self.input_data['end_node']] <= m[r], name='6arrival_lastblock' + '_' + str(r))

        # constraint 7: departure constraints
        if self.operating_mode == 0:
            for r in self.input_data['existing_trains'].keys():
                for s in O[r]:
                    for b in self.input_data['station_blocks'][s]:
                        model.addConstr(self.input_data['departure_times'][r, b] * u[r, b] + z[r, b] <= d[r, b],
                                        name="7departure" + '_' + str(r) + '_' + str(s) + '_' + str(b))

        # constraint 8: tight arrival constraint if trains follow each other
        for r in self.input_data['trains']:
            for rr in self.input_data['trains']:
                if r != rr:
                    for b in list(self.input_data['blocks']):
                        model.addConstr(d[r, b]<= a[rr, b] + (1 - x[r, rr, b]) * self.input_data['timehorizon'],
                                        name="8followingtrain" + '_' + str(r) + '_' + str(rr) + '_' + str(b))

        # constraint 9: only one successor for each train on each block (if the train uses that block)
        for r in R1:
            for b in list(self.input_data['blocks']):
                if r in self.input_data['trains']:
                    model.addConstr(sum(x[r, rr, b] for rr in R2 if r != rr) == u[r, b],
                                    name="9onesuccessor" + '_' + str(r) + '_' + str(b))
                else:
                    model.addConstr(sum(x[r, rr, b] for rr in R2 if r != rr) == 1,
                                    name="9onesuccessor" + '_' + str(r) + '_' + str(b))

        # constraint 10: only one predecessor for each train on each block (if the train uses that block
        for rr in R2:
            for b in list(self.input_data['blocks']):
                if rr in self.input_data['trains']:
                    model.addConstr(sum(x[r, rr, b] for r in R1 if r != rr) == u[rr, b],
                                    name="10onepredecessor" + '_' + str(rr) + '_' + str(b))
                else:
                    model.addConstr(sum(x[r, rr, b] for r in R1 if r != rr) == 1,
                                    name="10onepredecessor" + '_' + str(rr) + '_' + str(b))

        # constraint 11a: enforce starting at the beginning of the network
        if self.operating_mode:
            for r in self.input_data['trains']:
                model.addConstr(
                    a[r, list(self.input_data['blocks'])[0]] >= self.input_data['existing_trains'][r]['start'],
                    name="11start_network" + '_' + str(r))
        else:
            for r in self.input_data['existing_trains']:
                model.addConstr(a[r, list(self.input_data['blocks'])[0]] >= self.input_data['existing_trains'][r]['start'],
                                name="11start_network" + '_' + str(r))
            # model.addConstr(u[r,B[0]] == 1)
            # model.addConstr(d[r,B[0]] >= data['existing_trains'][r]['start'])
        # constraint 11b:
        if not self.operating_mode:
            for r in self.input_data['new_trains_traveltimes']:
                model.addConstr(
                    a[r, self.input_data['start_node']] >= self.input_data['new_trains_traveltimes'][r]['start'],
                    name="11start_network" + '_' + str(r))
                # model.addConstr(u[r, B[0]] == 1)
                # model.addConstr(d[r, B[0]] >= data['new_trains_traveltimes'][r]['start'])

        # constraint 12: only one track used in parallel cases -> general case of constraint 4
        for r in self.input_data['trains']:
            for l in self.input_data['layers']:
                model.addConstr(sum(u[r, ps] for ps in l) <= 1, name="12no_parallel" + '_' + str(r) + '_' + str(l))

        # constraints 13: fix variables
        if self.mip_mode == 1:
            for r in list(self.input_data['existing_trains'].keys()):
                # for stations
                for s in O[r]:
                    model.addConstr(
                        sum(a[r, b] for b in self.input_data['station_blocks'][s]) ==
                        self.input_data['existing_trains'][r]['arrival_times'][self.input_data['station_blocks'][s][0]])
                    model.addConstr(
                        sum(d[r, b] for b in self.input_data['station_blocks'][s]) ==
                        self.
                        input_data['existing_trains'][r]['departure_times'][self.input_data['station_blocks'][s][0]])
                #  for last block
                model.addConstr(a[r, self.input_data['end_node']] ==
                                self.input_data['existing_trains'][r]['arrival_times'][self.input_data['end_node']])

        self.time_dict['mip_creation_time'] = time.time() - start_time
        self.model = model

    def solve_model(self):
        start_time = time.time()
        self.model.optimize()
        self.time_dict['mip_solving_time'] = time.time() - start_time
        self.time_dict['mip_execution_time'] = self.time_dict['mip_creation_time'] + self.time_dict['mip_solving_time']
        self.time_dict = {k: round(v, 2) for k, v in self.time_dict.items()}  # round all values to two decimals

    def get_solution_of_model(self):
        # read variables
        u = self.variable_references['u']
        a = self.variable_references['a']
        d = self.variable_references['d']
        x = self.variable_references['x']
        m = self.variable_references['m']
        if not self.operating_mode:
            y = self.variable_references['y']
            z = self.variable_references['z']
        """for r in self.input_data['trains'] + [9991]:
            for rr in self.input_data['trains'] + [9999]:
                for b in ['17', '17_1', '17_2']:  # self.input_data['blocks']:
                    if x[r, rr, b].X > 0.5:
                        print(str(r) + ' gets followed by ' + str(rr) + ' on block ' + b)"""

        if self.model.status == GRB.INFEASIBLE:
            self.model_status = 0
            start_time = 9999
            # if self.operating_mode:
            self.model.computeIIS()
            self.model.write('model.ilp')

            # Relax the constraints to make the model feasible
            print('The model is infeasible; relaxing the constraints')
            orig_num_vars = self.model.NumVars
            self.model.feasRelaxS(0, False, False, True)
            self.model.optimize()
            status = self.model.status
            if status in (GRB.INF_OR_UNBD, GRB.INFEASIBLE, GRB.UNBOUNDED):
                print('The relaxed model cannot be solved \
                       because it is infeasible or unbounded')
                sys.exit(1)

            if status != GRB.OPTIMAL:
                print('Optimization was stopped with status %d' % status)
                sys.exit(1)

            print('\nSlack values:')
            slacks = self.model.getVars()[orig_num_vars:]
            for sv in slacks:
                if sv.X > 1e-6:
                    print('%s = %g' % (sv.VarName, sv.X))
        elif self.model.status == GRB.TIME_LIMIT:
            self.model_status = 0
            self.time_dict['mip_solving_time'] = self.model.MIPGap
            print('model has reached time limit')
        else:
            self.model_status = 1
            # print output in a readable format

            # print objective variables
            if self.print_solution == 2:
                AS = set()  # actual stops
                for s in self.input_data['stations']:
                    for b in self.input_data['station_blocks'][s]:
                        AS.add(b)
                for r in self.input_data['trains']:
                    impact = 0
                    if m[r].X > 0.5:
                        print('train ' + r + ' arrives ' + str(m[r].X) + ' late.')
                        impact += m[r].X
                    for b in AS:
                        if y[r, b].X > 0.5:
                            print('train ' + r + ' arrives ' + str(y[r, b].X) + ' late at ' + b)
                            impact += y[r, b].X
                        if z[r, b].X > 0.5:
                            print('train ' + r + ' departures ' + str(z[r, b].X) + ' late from ' + b)
                            impact += z[r, b].X
                    if impact > 0:
                        print('impact on objective: ' + str(impact))

            # print block wise
            if self.print_solution == 2:
                for l in self.input_data['layers']:
                    for b in l:
                        print('\nblock ' + str(b))
                        for r in self.input_data['trains']:
                            if u[r, b].X > 0.5:
                                print(str(r) + ': at ' + str(a[r, b].X) + ' dt ' + str(d[r, b].X))

            # fetch actual travel times for trains to construct a feasible timetable
            # if self.operating_mode == 1:
            self.resulting_timetable = {}
            for r in self.input_data['trains']:
                self.resulting_timetable[r] = {}
                self.resulting_timetable[r]['traveltimes'] = {}
                self.resulting_timetable[r]['arrival_times'] = {}
                self.resulting_timetable[r]['departure_times'] = {}
                self.resulting_timetable[r]['start'] = int(a[r, self.input_data['start_node']].X)
                self.resulting_timetable[r]['end'] = int(a[r, self.input_data['end_node']].X)
                # fetch traveltimes
                for (sb, eb) in self.input_data['edges']:
                    if u[r, sb].X > 0.5 and u[r, eb].X > 0.5:
                        sb_number = sb.split('_')[0].split('#')[0]
                        eb_number = eb.split('_')[0].split('#')[0]
                        assert ('#' not in eb or '#' not in sb)
                        if '#' in eb:
                            self.resulting_timetable[r]['traveltimes'][(sb_number, sb_number)] = int(
                                d[r, sb].X - a[r, sb].X)
                        elif '#' in sb:
                            self.resulting_timetable[r]['traveltimes'][(sb_number, eb_number)] = int(
                                d[r, sb].X - a[r, sb].X)
                        else:
                            self.resulting_timetable[r]['traveltimes'][(sb_number, eb_number)] = int(
                                d[r, sb].X - a[r, sb].X)
                # fetch arrival and departure times
                for s in self.input_data['stations']:
                    self.resulting_timetable[r]['arrival_times'][s] = int(
                        max(a[r, b].X for b in self.input_data['station_blocks'][s]))  # for stations
                    self.resulting_timetable[r]['departure_times'][s] = int(
                        max(d[r, b].X for b in self.input_data['station_blocks'][s]))  # for stations
                # arrival time for last block
                self.resulting_timetable[r]['arrival_times'][self.input_data['end_node']] = int(
                    a[r, self.input_data['end_node']].X)

        self.time_dict = {k: round(v, 2) for k, v in self.time_dict.items()}
        print('mip execution time: ' + str(self.time_dict['mip_execution_time']) + 's')
