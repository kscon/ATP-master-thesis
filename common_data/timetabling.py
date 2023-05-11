import copy
from MIP_train_timetable_problem.mip_model import MIPModel
from common_data import networks_utils


class Timetabling:
    def __init__(self, parsed_data, file_name_string=None):
        assert (file_name_string is not None) or (parsed_data is not None)
        self.file_name_string = file_name_string
        self.input_data = parsed_data
        self.result_timetable = None

    def check_timetable_feasibility(self):
        if not (len(list(self.input_data['existing_trains'].keys())) > 5 or \
                len(list(self.input_data['new_trains_traveltimes'].keys())) > 5):
            # test with global mode to generate large instances
            mip = MIPModel(parsed_data=self.input_data, filepath=self.file_name_string,
                           operating_mode=1, mip_mode=0, print_solution=0)
            mip.execute_full_model()
            self.result_timetable = mip.resulting_timetable
        else:
            # test with iterative mode to generate large instances

            """ex_trains_keys = list(self.input_data['existing_trains'].keys())
            iteration_counter = 0

            # in each iteration add one of the new trains and add it to the fixed timetable from the last iteration
            parsed_data_iteration = copy.deepcopy(self.input_data)
            parsed_data_iteration['trains'] = []

            for etk in ex_trains_keys:
                iteration_counter += 1
                # parsed_data_iteration['new_trains_traveltimes'] = {}

                # parsed_data_iteration['existing_trains'][etk] = self.input_data['existing_trains'][etk]
                parsed_data_iteration['trains'].append(etk)

                mip = MIPModel(parsed_data=parsed_data_iteration, filepath=self.file_name_string, operating_mode=1,
                               mip_mode=0, print_solution=1)
                mip.execute_full_model()
                assert mip.model_status

                parsed_data_iteration['existing_trains'][etk] = copy.deepcopy(
                    parsed_data_iteration['existing_trains'][etk])

                for r in mip.resulting_timetable.keys():
                    parsed_data_iteration['existing_trains'][r]['start'] = mip.resulting_timetable[r]['start']
                    parsed_data_iteration['existing_trains'][r]['traveltimes'] = mip.resulting_timetable[r][
                        'traveltimes']
                    parsed_data_iteration['existing_trains'][r]['arrival_times'] = mip.resulting_timetable[r][
                        'arrival_times']
                    parsed_data_iteration['existing_trains'][r]['departure_times'] = \
                        mip.resulting_timetable[r]['departure_times']"""

            parsed_data = self.input_data.copy()

            ex_trains_keys = list(parsed_data['existing_trains'].keys())
            iteration_counter = 0



            # in each iteration add one of the new trains and add it to the fixed timetable from the last iteration
            parsed_data_iteration = copy.deepcopy(parsed_data)
            parsed_data_iteration['trains'] = []
            parsed_data_iteration['existing_trains'] = {}

            mip_time_dict = {}
            for ntk in ex_trains_keys:
                iteration_counter += 1
                parsed_data_iteration['new_trains_traveltimes'] = {}

                parsed_data_iteration['new_trains_traveltimes'][ntk] = parsed_data['existing_trains'][ntk]
                parsed_data_iteration['trains'].append(ntk)

                mip = MIPModel(parsed_data=parsed_data_iteration, filepath=self.file_name_string, operating_mode=0,
                               mip_mode=1, print_solution=1)
                mip.execute_full_model()
                assert mip.model_status


                parsed_data_iteration['existing_trains'][ntk] = copy.deepcopy(
                    parsed_data['existing_trains'][ntk])

                for r in mip.resulting_timetable.keys():
                    parsed_data_iteration['existing_trains'][r]['start'] = mip.resulting_timetable[r]['start']
                    parsed_data_iteration['existing_trains'][r]['traveltimes'] = mip.resulting_timetable[r][
                        'traveltimes']
                    parsed_data_iteration['existing_trains'][r]['arrival_times'] = mip.resulting_timetable[r][
                        'arrival_times']
                    parsed_data_iteration['existing_trains'][r]['departure_times'] = \
                        mip.resulting_timetable[r]['departure_times']

            self.result_timetable = mip.resulting_timetable

    def compare_generated_and_feasible_timetable(self):
        print('##### data comparison #####\ntrain/block: generated --> feasible')
        for r in self.input_data['existing_trains'].keys():
            print('\n' + r)
            val_gen = self.input_data['existing_trains'][r]['start']
            val_fea = self.result_timetable[r]['start']
            if val_gen != val_fea:
                print('start: ' + str(val_gen) + '-->' + str(int(val_fea)))
            # print('# block travel times')
            for b in sorted(self.input_data['existing_trains'][r]['traveltimes'].keys()):
                val_gen = self.input_data['existing_trains'][r]['traveltimes'][b]
                val_fea = self.result_timetable[r]['traveltimes'][b]
                if val_gen != val_fea:
                    print(str(b) + ' tt: ' + str(val_gen) + '-->' + str(int(val_fea)))
            for b in self.input_data['existing_trains'][r]['arrival_times'].keys():
                val_gen = self.input_data['existing_trains'][r]['arrival_times'][b]
                val_fea = self.result_timetable[r]['arrival_times'][b]
                if val_gen != val_fea:
                    print(str(b) + ' at: ' + str(val_gen) + '-->' + str(int(val_fea)))
            for b in self.input_data['existing_trains'][r]['departure_times'].keys():
                val_gen = self.input_data['existing_trains'][r]['departure_times'][b]
                val_fea = self.result_timetable[r]['departure_times'][b]
                if val_gen != val_fea:
                    print(str(b) + ' dt: ' + str(val_gen) + '-->' + str(int(val_fea)))

    def overwrite_current_with_feasible_timetable(self):
        for r in self.input_data['existing_trains'].keys():
            self.input_data['existing_trains'][r]['start'] = self.result_timetable[r]['start']
            self.input_data['existing_trains'][r]['traveltimes'] = self.result_timetable[r]['traveltimes']
            self.input_data['existing_trains'][r]['arrival_times'] = self.result_timetable[r]['arrival_times']
            self.input_data['existing_trains'][r]['departure_times'] = \
                self.result_timetable[r]['departure_times']
