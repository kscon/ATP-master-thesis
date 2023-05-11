import numpy as np
from common_data.timetabling import Timetabling
from MIP_train_timetable_problem import mip_input_parser


class NetworkGenerator:
    def __init__(self, number_of_blocks: int = 0, small_stations: int = 0, big_stations: int = 0,
                 slow_trains: int = 0, fast_trains: int = 0, new_trains: list = None, file_location: str = ''):
        self.data = {}
        self.parameters = {'number_of_blocks': number_of_blocks,
                           'small_stations': small_stations,
                           'big_stations': big_stations,
                           'slow_trains': slow_trains,
                           'fast_trains': fast_trains,
                           'new_trains': new_trains,
                           }
        self.filled_sequence = []
        self.file_name_string = file_location
        self.result_timetable = None

    def generate_network(self):
        occupied_blocks = 3 * self.parameters['small_stations'] + 3 * self.parameters['big_stations']
        assert (self.parameters['number_of_blocks'] - occupied_blocks >= 0)

        # 0 = signal, 1 = switch, 2 = small stations, 3 = big stations
        sequence = np.concatenate(
            (2 * np.ones(self.parameters['small_stations'], dtype=int),
             3 * np.ones(self.parameters['big_stations'], dtype=int),
             np.zeros(self.parameters['number_of_blocks'] - occupied_blocks - 1, dtype=int)))
        # print(sequence)
        sequence_perm = np.random.permutation(sequence)
        # print(sequence_perm)

        # filled_sequence = []
        for s in sequence_perm:
            if s == 0:
                self.filled_sequence.append(s)
            elif s == 2:
                self.filled_sequence.extend([1, 2, 1])
            elif s == 3:
                self.filled_sequence.extend([1, 3, 1])
        self.filled_sequence.append(0)

        # print('filled_sequence:', self.filled_sequence, len(self.filled_sequence))

        self.data['nodes'] = [str(i) for i in range(len(self.filled_sequence))]
        self.data['start_node'] = self.data['nodes'][0]
        self.data['end_node'] = self.data['nodes'][-1]
        self.data['edges'] = [(self.data['nodes'][i], self.data['nodes'][i + 1]) for i in
                              range(len(self.data['nodes']) - 1)]
        self.data['nodes_labels'] = {}
        for i in range(len(self.filled_sequence)):
            if self.filled_sequence[i] == 0:
                self.data['nodes_labels'][self.data['nodes'][i]] = 'signal'
            elif self.filled_sequence[i] == 1:
                self.data['nodes_labels'][self.data['nodes'][i]] = 'switch'
            elif self.filled_sequence[i] == 2 or self.filled_sequence[i] == 3:
                self.data['nodes_labels'][self.data['nodes'][i]] = 'station'

        # print(data['nodes'])
        # print(data['edges'])

    def generate_capacities(self):
        self.data['capacities'] = {}
        pending_capacity = 1
        for i in range(len(self.filled_sequence) - 1):
            if self.filled_sequence[i] == 0:
                self.data['capacities'][(str(i), str(i + 1))] = 1
                pending_capacity = 1
            elif self.filled_sequence[i] == 1:
                if pending_capacity == 1:
                    if self.filled_sequence[i + 1] == 2:
                        pending_capacity = np.random.default_rng().integers(1, 3)
                    elif self.filled_sequence[i + 1] == 3:
                        pending_capacity = np.random.default_rng().integers(2, 5)
                    self.data['capacities'][(str(i), str(i))] = 1
                    self.data['capacities'][(str(i), str(i + 1))] = pending_capacity
                else:
                    pending_capacity = 1
                    self.data['capacities'][(str(i), str(i))] = pending_capacity
                    self.data['capacities'][(str(i), str(i + 1))] = pending_capacity
            elif self.filled_sequence[i] == 2 or self.filled_sequence[i] == 3:
                self.data['capacities'][(str(i), str(i))] = pending_capacity
                self.data['capacities'][(str(i), str(i + 1))] = pending_capacity
            else:
                raise Exception

        # print(data['capacities'])

    def generate_traveltimes(self):
        # generate traveltimes for slow and fast trains
        self.data['existing_trains'] = {}
        self.data['new_trains_traveltimes'] = {}

        # fast trains:
        fast_trains_traveltimes = {}
        for (sb, eb) in self.data['capacities'].keys():
            if sb == eb and self.filled_sequence[self.data['nodes'].index(sb)] == 3:
                fast_trains_traveltimes[(sb, eb)] = 10
            else:
                fast_trains_traveltimes[(sb, eb)] = 1

        # set self.data
        for r in range(self.parameters['fast_trains']):
            train_name = 'ICE_' + str(r)
            self.data['existing_trains'][train_name] = {}
            self.data['existing_trains'][train_name]['start'] = 1 + r * 20
            self.data['existing_trains'][train_name]['traveltimes'] = fast_trains_traveltimes

        # slow trains:
        slow_trains_traveltime = {}
        for (sb, eb) in self.data['capacities'].keys():
            if sb == eb and self.filled_sequence[self.data['nodes'].index(sb)] == 2:
                slow_trains_traveltime[(sb, eb)] = 2
            elif sb == eb and self.filled_sequence[self.data['nodes'].index(sb)] == 3:
                slow_trains_traveltime[(sb, eb)] = 4
            else:
                slow_trains_traveltime[(sb, eb)] = np.random.randint(1, 3)

        # set self.data
        for r in range(self.parameters['slow_trains']):
            train_name = 'RE_' + str(r)
            self.data['existing_trains'][train_name] = {}
            self.data['existing_trains'][train_name]['start'] = 11 + r * 20
            self.data['existing_trains'][train_name]['traveltimes'] = slow_trains_traveltime

        t_max = 0
        # get arrival and departure times for existing trains
        for r in self.data['existing_trains'].keys():
            self.data['existing_trains'][r]['arrival_times'] = {}
            self.data['existing_trains'][r]['departure_times'] = {}
            t = self.data['existing_trains'][r]['start']
            for (sb, eb) in self.data['capacities'].keys():
                if sb == eb and self.data['nodes_labels'][sb] == 'station':
                    self.data['existing_trains'][r]['arrival_times'][sb] = t

                t += self.data['existing_trains'][r]['traveltimes'][(sb, eb)]

                if sb == eb and self.data['nodes_labels'][sb] == 'station':
                    self.data['existing_trains'][r]['departure_times'][sb] = t

                if eb == self.data['end_node']:
                    self.data['existing_trains'][r]['arrival_times'][eb] = t

            if t > t_max:
                t_max = t

        # new_train traveltimes
        new_train_counter = 0
        for r in self.parameters['new_trains']:
            train_name = 'new_train_' + r + '_' + str(new_train_counter)
            self.data['new_trains_traveltimes'][train_name] = {}
            self.data['new_trains_traveltimes'][train_name]['start'] = 5 + 10 * new_train_counter

            if r == 's':
                self.data['new_trains_traveltimes'][train_name]['traveltimes'] = slow_trains_traveltime
            elif r == 'f':
                self.data['new_trains_traveltimes'][train_name]['traveltimes'] = fast_trains_traveltimes
            new_train_counter += 1

        # get arrival and departure times for new train
        for r in self.data['new_trains_traveltimes'].keys():
            self.data['new_trains_traveltimes'][r]['arrival_times'] = {}
            self.data['new_trains_traveltimes'][r]['departure_times'] = {}
            t = self.data['new_trains_traveltimes'][r]['start']
            for (sb, eb) in self.data['capacities'].keys():
                if sb == eb and self.data['nodes_labels'][sb] == 'station':
                    self.data['new_trains_traveltimes'][r]['arrival_times'][sb] = t

                t += self.data['new_trains_traveltimes'][r]['traveltimes'][(sb, eb)]

                if sb == eb and self.data['nodes_labels'][sb] == 'station':
                    self.data['new_trains_traveltimes'][r]['departure_times'][sb] = t

                if eb == self.data['end_node']:
                    self.data['new_trains_traveltimes'][r]['arrival_times'][eb] = t

            if t > t_max:
                t_max = t

        # print(t_max)
        self.data['timehorizon'] = int(1.2 * t_max)

    def generate_filestring(self):
        file_name_string = str(self.parameters['number_of_blocks']) + 'b_' + str(
            self.parameters['small_stations'] + self.parameters['big_stations']) + 's_' + \
                           str(self.parameters['slow_trains'] + self.parameters['fast_trains']) + 'et_' + \
                           str(len(self.parameters['new_trains'])) + 'nt_' + str(
            self.data['timehorizon']) + 't_' + str(np.random.randint(1, 1000))

        self.file_name_string += file_name_string

    def save_file(self):
        with open("common_data/networks/" + self.file_name_string + '.py', 'w') as f:
            f.write('data=' + str(self.data))

    # check_timetable_feasibility = 1: check whether the generated timetable of the existing trains is actually feasible
    # overwrite_generated_timetable = 1: overwrite generated timetable with feasible (only possible if
    # check_timetable_feasibility = 1)
    def run_network_generator(self, check_timetable_feasibility=0, overwrite_generated_timetable=0):
        self.generate_network()
        self.generate_capacities()
        self.generate_traveltimes()
        self.generate_filestring()

        if check_timetable_feasibility:
            parsed_data = mip_input_parser.parse_input(filepath=self.file_name_string,
                                                       operating_mode=1, unparsed_data=self.data.copy())
            tt = Timetabling(parsed_data=parsed_data, file_name_string=self.file_name_string)
            tt.check_timetable_feasibility()
            tt.compare_generated_and_feasible_timetable()
            if overwrite_generated_timetable:
                tt.overwrite_current_with_feasible_timetable()
                self.data['existing_trains'] = tt.input_data['existing_trains']

        self.save_file()
        print('done')
