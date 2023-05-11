import networkx as nx
import itertools
import copy
from typing import Dict


class TEN:
    def __init__(self, data: dict, print_solution=0):
        self.ten = nx.DiGraph()
        self.ten_helper = nx.DiGraph()
        self.nrg = data['graph']
        self.data = data
        self.print_solution = print_solution
        self.resulting_path = None
        self.resulting_timetable = None

        if len(list(self.data['new_trains_traveltimes'].keys())) > 1:
            print('TEN-Warning: new trains list has more than one entry ')
        self.new_train = list(self.data['new_trains_traveltimes'].keys())[0]

        self.construct_ten_helper()
        self.construct_ten()

    # construct a ten helper graph displaying the ten for one timestep
    def construct_ten_helper(self):
        # generate network representing one timestep of the TEN
        layer = 0
        for v in nx.nodes(self.nrg):
            if self.data['nodes_labels'][v] == 'station' or self.data['nodes_labels'][v] == 'switch':
                self.ten_helper.add_node(str(v), layer=layer)
                layer += 1
                self.ten_helper.add_node(str(v) + '#', layer=layer)
                layer += 1
                self.ten_helper.add_edge(str(v), str(v) + '#',
                                         weight=self.data['new_trains_traveltimes'][self.new_train]
                                         ['traveltimes'][(v, v)],
                                         capacity=self.data['capacities'][(v, v)])
            elif self.data['nodes_labels'][v] == 'signal':
                self.ten_helper.add_node(str(v), layer=layer)
                layer += 1

        for (v1, v2) in nx.edges(self.nrg):
            if self.data['nodes_labels'][v1] == 'station' or self.data['nodes_labels'][v1] == 'switch':
                self.ten_helper.add_edge(str(v1) + '#', str(v2),
                                         weight=self.data['new_trains_traveltimes'][self.new_train]
                                         ['traveltimes'][(v1, v2)],
                                         capacity=self.data['capacities'][(v1, v2)])
            else:
                self.ten_helper.add_edge(str(v1), str(v2),
                                         weight=self.data['new_trains_traveltimes']
                                         [self.new_train]['traveltimes'][(v1, v2)],
                                         capacity=self.data['capacities'][(v1, v2)])

    # construct the ten (for a single train)
    def construct_ten(self):
        # generate nodes for all timesteps
        for t in range(self.data['timehorizon']):
            for v in sorted(nx.nodes(self.ten_helper)):
                layer = self.ten_helper.nodes[v]['layer']
                self.ten.add_node(str(v) + '_' + str(t), layer=layer)

        # generate edges for all timesteps
        for (v1, v2) in nx.edges(self.ten_helper):
            weight = self.ten_helper[v1][v2]['weight']
            for t in range(self.data['timehorizon'] - weight):
                self.ten.add_edge(str(v1) + '_' + str(t), str(v2) + '_' + str(t + weight),
                                  capacity=self.ten_helper.edges[(v1, v2)]['capacity'], flow=0)

        # generate waiting edges
        for v in nx.nodes(self.ten_helper) - [self.data['end_node']]:
            edges = [(w, n) for (w, n) in self.ten_helper.edges() if v == w]
            capacity = max([c for (v1, v2, c) in self.ten_helper.edges.data('capacity') if (v1, v2) in edges])
            for t in range(self.data['timehorizon'] - 1):
                self.ten.add_edge(str(v) + '_' + str(t), str(v) + '_' + str(t + 1),
                                  capacity=capacity, flow=0)

    # add existing timetable
    # add auxialry flow/edges in the ten to caputure existing timetable.
    # for each train we receive traveltimes of the same format as the traveltimes of the new train
    def add_existing_timetable_to_ten(self):
        for key, z in self.data['existing_trains'].items():
            starttime = z['start']
            for (t_a, t_e) in self.data['capacities'].keys():
                traveltime = z['traveltimes'][(t_a, t_e)]
                # check whether edges would be outside of time scope
                if starttime + traveltime >= self.data['timehorizon']:
                    break

                # determine start and end nodes for the new edge
                node_start = ''
                node_end = ''

                if t_a == t_e:
                    # current element is a switch or station
                    node_start = str(t_a) + '_' + str(starttime)
                    node_end = str(t_e) + '#_' + str(starttime + traveltime)
                else:
                    # determine whether we start from a signal or a switch/station
                    if self.data['nodes_labels'][t_a] == 'signal':
                        node_start = str(t_a) + '_' + str(starttime)
                    else:
                        node_start = str(t_a) + '#_' + str(starttime)
                    node_end = str(t_e) + '_' + str(starttime + traveltime)

                # check if edge exists
                if (node_start, node_end) in nx.edges(self.ten):
                    self.ten.edges[(node_start, node_end)]['flow'] += 1
                else:  # otherwise add temporary edge
                    self.ten.add_edge(node_start, node_end, capacity=0, flow=1, aux=1)
                starttime += traveltime

    # step 3 of the algorithm
    def edge_preprocessing(self):
        self.advanced_edge_deletion()
        self.simple_edge_deletion()

    # simple edge deletion procedure
    def simple_edge_deletion(self):
        # delete edges that are "simple" to find
        aux_set = [(u, v) for (u, v, aux) in self.ten.edges.data('aux') if aux == 1]
        for v in self.ten.nodes():
            # in_edges = [e for e in self.ten.in_edges(v) if e not in aux_set]
            out_edges = [e for e in self.ten.out_edges(v) if e not in aux_set]
            if len(out_edges) == 0:
                continue
            out_capacity = min([self.ten.edges[(a, b)]['capacity'] for (a, b) in out_edges if
                                self.ten.edges[(a, b)]['capacity'] > 0])
            out_flow = sum([self.ten.edges[(a, b)]['flow'] for (a, b) in out_edges])

            # check whether the capacity of all outgoing edges is the same number n for all edges
            if out_flow >= out_capacity:
                self.ten.remove_edges_from(out_edges)
        # remove aux set edges
        self.ten.remove_edges_from(aux_set)

    # advanced edge deletion procedure
    def advanced_edge_deletion(self):
        aux_set = [(u, v) for (u, v, aux) in self.ten.edges.data('aux') if aux == 1]

        for (u, v) in aux_set:
            start_node, start_time = str(u).split('_')
            end_node, end_time = str(v).split('_')
            start_time = int(start_time)
            end_time = int(end_time)
            start_node_blank = start_node.split('#')[0]
            end_node_blank = end_node.split('#')[0]

            r = self.data['new_trains_traveltimes'][self.new_train]['traveltimes'][(start_node_blank, end_node_blank)]
            iteration_range = None
            if end_time - start_time > r:
                # delete edges where new train is faster than existing train
                iteration_range = range(start_time, end_time - r + 1)
            elif end_time - start_time < r:
                # delete edges where new train is slower than existing train
                iteration_range = range(start_time - (r - (end_time - start_time)), start_time + 1)

            # second attempt: delete all in one algorithm
            for j in iteration_range:
                current_node = str(start_node) + '_' + str(j)
                if len(self.ten.out_edges(current_node)) == 0:
                    continue
                edge_capacity = max([cap for (a, b, cap) in self.ten.out_edges(current_node, data='capacity')])
                aux_set_j = [(u, v) for (u, v) in self.ten.edges() if u.split('_')[0] == start_node and
                             ((u, v) in aux_set or self.ten.edges[u, v]['flow'] > 0) and
                             int(u.split('_')[1]) <= j + r and int(v.split('_')[1]) >= j]
                if len(aux_set_j) >= edge_capacity:
                    edges_to_delete = [e for e in self.ten.out_edges(current_node) if e not in aux_set]
                    self.ten.remove_edges_from(edges_to_delete)

    # pathfinding loop
    def pathfinding(self):
        start_time = self.data['new_trains_traveltimes'][list(self.data['new_trains_traveltimes'].keys())[0]]['start']
        start_node = str(self.data['nodes'][0]) + '_' + str(start_time)
        end_node = self.data['nodes'][-1]
        planned_arrival_time = int(end_node.split('_')[-1])

        found_path = 0
        # loop over possible start node, in case a path can not be found at the intended start time
        while not found_path:
            # now fixed start node, find path
            for i in range(planned_arrival_time, self.data['timehorizon']):
                try:
                    end_node = end_node.split('_')[0] + '_' + str(i)
                    self.resulting_path = nx.shortest_path(self.ten, source=start_node, target=end_node)
                    found_path = 1
                    break
                except nx.NetworkXNoPath:
                    if self.print_solution:
                        print('Path starting at ' + start_node + ' and ending in ' + end_node + ' could not be found')

            # a path for the intended start time could not be found, try the next time
            start_time += 1
            start_node = str(self.data['nodes'][0]) + '_' + str(start_time)

    def generate_timetable_from_path(self):
        self.resulting_timetable = {}
        for r in self.data['existing_trains'].keys():
            self.resulting_timetable[r] = self.data['existing_trains'][r]

        new_train = list(self.data['new_trains_traveltimes'].keys())[0]
        self.resulting_timetable[new_train] = {}
        self.resulting_timetable[new_train]['traveltimes'] = {}
        self.resulting_timetable[new_train]['arrival_times'] = {}
        self.resulting_timetable[new_train]['departure_times'] = {}
        self.resulting_timetable[new_train]['start'] = int(self.resulting_path[0].split('_')[-1])
        self.resulting_timetable[new_train]['end'] = int(self.resulting_path[-1].split('_')[-1])

        # clean path of waiting edges
        clean_path = copy.deepcopy(self.resulting_path)
        for sn, en in itertools.pairwise(self.resulting_path):
            start_block = sn.split('_')[0]
            # start_time = int(sn.split('_')[-1])
            end_block = en.split('_')[0]
            # end_time = int(en.split('_')[-1])
            if start_block == end_block:
                clean_path.remove(en)

        for sn, en in itertools.pairwise(clean_path):
            start_block = sn.split('_')[0].split('#')[0]
            start_time = int(sn.split('_')[-1])
            end_block = en.split('_')[0].split('#')[0]
            end_time = int(en.split('_')[-1])

            # cover cases of waiting edges/nodes, e.g. ..., 7_23, 7_24, 7#_25,... In that case add one to the traveltime
            if (start_block, end_block) in self.resulting_timetable[new_train]['traveltimes'].keys():
                self.resulting_timetable[new_train]['traveltimes'][(start_block, end_block)] += 1
                continue
            else:
                self.resulting_timetable[new_train]['traveltimes'][(start_block, end_block)] = end_time - start_time

            if self.data['nodes_labels'][start_block] == 'station':
                if start_block == end_block:
                    self.resulting_timetable[new_train]['arrival_times'][start_block] = start_time
                else:
                    self.resulting_timetable[new_train]['departure_times'][start_block] = end_time

            if end_block == self.data['end_node']:
                self.resulting_timetable[new_train]['arrival_times'][end_block] = end_time
