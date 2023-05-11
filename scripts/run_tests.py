import os
import copy
import pandas as pd
from MIP_train_timetable_problem.mip_model import MIPModel
from MIP_train_timetable_problem import mip_input_parser
from TEN_additional_train_path_problem.ten_model import TENModel
from TEN_additional_train_path_problem import ten_input_parser
import plot_utils


# test the mip with iterative mode
def mip_iteratively(filepath, plot_timetable=0, print_solution=0):
    print('> running mip iteratively...')
    parsed_data = mip_input_parser.parse_input(filepath=filepath, operating_mode=0)

    new_trains_keys = list(parsed_data['new_trains_traveltimes'].keys())
    iteration_counter = 0

    if plot_timetable:
        plot_utils.render_timetable({'timetable': parsed_data['existing_trains'], 'layers': parsed_data['layers'],
                                     'model': 'mip', 'model_mode': 'iterative',
                                     'timehorizon': parsed_data['timehorizon'], 'filepath': filepath,
                                     'iteration_counter': iteration_counter})

    # in each iteration add one of the new trains and add it to the fixed timetable from the last iteration
    parsed_data_iteration = copy.deepcopy(parsed_data)
    parsed_data_iteration['trains'] = [t for t in parsed_data['trains'] if t not in new_trains_keys]

    mip_time_dict = {}
    for ntk in new_trains_keys:
        iteration_counter += 1
        parsed_data_iteration['new_trains_traveltimes'] = {}

        parsed_data_iteration['new_trains_traveltimes'][ntk] = parsed_data['new_trains_traveltimes'][ntk]
        parsed_data_iteration['trains'].append(ntk)

        mip = MIPModel(parsed_data=parsed_data_iteration, filepath=filepath, operating_mode=0, mip_mode=1,
                       print_solution=print_solution)
        mip.execute_full_model()
        assert mip.model_status

        mip_time_dict[iteration_counter] = mip.time_dict

        if plot_timetable:
            plot_utils.render_timetable({'timetable': mip.resulting_timetable,
                                         'layers': parsed_data_iteration['layers'],
                                         'model': 'mip', 'model_mode': 'iterative',
                                         'timehorizon': parsed_data_iteration['timehorizon'],
                                         'filepath': filepath,
                                         'iteration_counter': iteration_counter})

        parsed_data_iteration['existing_trains'][ntk] = copy.deepcopy(
            parsed_data_iteration['new_trains_traveltimes'][ntk])

        for r in mip.resulting_timetable.keys():
            parsed_data_iteration['existing_trains'][r]['start'] = mip.resulting_timetable[r]['start']
            parsed_data_iteration['existing_trains'][r]['traveltimes'] = mip.resulting_timetable[r]['traveltimes']
            parsed_data_iteration['existing_trains'][r]['arrival_times'] = mip.resulting_timetable[r][
                'arrival_times']
            parsed_data_iteration['existing_trains'][r]['departure_times'] = \
                mip.resulting_timetable[r]['departure_times']

    print('mip iteratively done!')
    return mip_time_dict


# test the mip with global mode
def mip_globally(filepath, plot_timetable=0, print_solution=0):
    print('> running mip globally...')
    parsed_data = mip_input_parser.parse_input(filepath=filepath, operating_mode=0)
    mip = MIPModel(parsed_data=parsed_data, filepath=filepath,
                   operating_mode=0, mip_mode=1, print_solution=print_solution)
    mip.execute_full_model()

    if plot_timetable and mip.model_status == 1:
        plot_utils.render_timetable({'timetable': mip.resulting_timetable,
                                     'layers': parsed_data['layers'], 'model': 'mip', 'model_mode': 'global',
                                     'timehorizon': parsed_data['timehorizon'],
                                     'filepath': filepath,
                                     'iteration_counter': 1})

    print('mip globally done!')
    return {0: mip.time_dict}


# test the ten with iterative mode (no global mode)
# plot_timetable, print_solution, draw_tens: 0-1; drawing_timehorizon: a <= b
def ten_iteratively(filepath, plot_timetable=0, draw_tens=0, drawing_timehorizon=(25, 35), print_solution=0):
    print('> running ten iteratively...')
    parsed_data = ten_input_parser.parse_input(filepath)
    # ten_model = TENModel(parsed_data=parsed_data, filepath=filepath, draw_tens=0, print_solution=0)

    new_trains_keys = list(parsed_data['new_trains_traveltimes'].keys())
    iteration_counter = 0

    if plot_timetable:
        plot_utils.render_timetable({'timetable': parsed_data['existing_trains'], 'model': 'ten',
                                     'layers': parsed_data['layers'], 'timehorizon': parsed_data['timehorizon'],
                                     'filepath': filepath, 'iteration_counter': iteration_counter})

    # in each iteration add one of the new trains and add it to the fixed timetable from the last iteration
    parsed_data_iteration = copy.deepcopy(parsed_data)
    parsed_data_iteration['trains'] = [t for t in parsed_data['trains'] if t not in new_trains_keys]

    ten_time_dict = {}
    for ntk in new_trains_keys:
        iteration_counter += 1
        parsed_data_iteration['new_trains_traveltimes'] = {}

        parsed_data_iteration['new_trains_traveltimes'][ntk] = parsed_data['new_trains_traveltimes'][ntk]
        parsed_data_iteration['trains'].append(ntk)

        ten_model = TENModel(parsed_data=parsed_data_iteration, iteration=iteration_counter,
                             filepath=filepath, draw_tens=draw_tens, print_solution=print_solution,
                             drawing_timehorizon=drawing_timehorizon)
        ten_model.execute_ten_model()

        ten_time_dict[iteration_counter] = ten_model.time_dict

        if plot_timetable:
            plot_utils.render_timetable({'timetable': ten_model.ten_core.resulting_timetable,
                                         'model': 'ten',
                                         'layers': ten_model.ten_core.data['layers'],
                                         'timehorizon': parsed_data['timehorizon'],
                                         'filepath': filepath,
                                         'iteration_counter': iteration_counter})

        parsed_data_iteration['existing_trains'][ntk] = copy.deepcopy(
            parsed_data_iteration['new_trains_traveltimes'][ntk])

        for r in ten_model.ten_core.resulting_timetable.keys():
            parsed_data_iteration['existing_trains'][r]['start'] = \
                ten_model.ten_core.resulting_timetable[r]['start']
            parsed_data_iteration['existing_trains'][r]['traveltimes'] = \
                ten_model.ten_core.resulting_timetable[r]['traveltimes']
            parsed_data_iteration['existing_trains'][r]['arrival_times'] = \
                ten_model.ten_core.resulting_timetable[r][
                    'arrival_times']
            parsed_data_iteration['existing_trains'][r]['departure_times'] = \
                ten_model.ten_core.resulting_timetable[r]['departure_times']

    print('ten iteratively done!')
    return ten_time_dict


# test mip and ten for one network (one train)
def run_on_file(filepath, models, plot_timetable):
    assert models != []
    filename = filepath.split('/')[-1]
    print('\n## testing: ' + filename)

    if not os.path.exists('output/' + filepath):
        os.makedirs('output/' + filepath)

    time_dicts = {}

    if 'ten_it' in models:
        time_dicts['ten_it'] = ten_iteratively(filepath=filepath, plot_timetable=plot_timetable, draw_tens=1)
    if 'mip_it' in models:
        time_dicts['mip_it'] = mip_iteratively(filepath=filepath, plot_timetable=plot_timetable)
    if 'mip_gl' in models:
        time_dicts['mip_gl'] = mip_globally(filepath=filepath, plot_timetable=plot_timetable)

    df_time_dicts = pd.DataFrame.from_dict({(i, j, k): time_dicts[i][j][k]
                                            for i in time_dicts.keys()
                                            for j in time_dicts[i].keys()
                                            for k in time_dicts[i][j].keys()},
                                           columns=[filepath.split('/')[-1]],
                                           orient='index').T
    #df_time_dicts.index = pd.MultiIndex.from_tuples(df_time_dicts.index)
    #df_time_dicts = df_time_dicts.T
    df_time_dicts.to_csv('output/' + filepath + '/execution_time_comparison_' + filepath.split('/')[-1] +
                         '_' + '_'.join(models) + '.csv')

    return df_time_dicts


# test mip and ten for all networks (one train)
# filename_filter: check if a substring is part of the filename. If not, do not include it in the loop
def run_on_folder(directory, models, filename_filter='', plot_timetable=0):
    assert models != []

    df_directory_time_dicts = pd.DataFrame()

    # test loop
    for filename in os.listdir(directory):
        if filename[-3:] == '.py' and filename_filter in filename:
            filepath = directory.split('/')[-1] + '/' + filename[:-3]  # without .py

            df_directory_time_dicts = \
                pd.concat([df_directory_time_dicts,
                           run_on_file(filepath=filepath, models=models, plot_timetable=plot_timetable)])

    filename_filter += '_'
    df_directory_time_dicts.to_csv('output/' + directory.split('/')[-1] +
                                   '/directory_execution_time_comparison_' + filename_filter + '_'.join(models)
                                   + '.csv')


# models=['ten_it', 'mip_it', 'mip_gl']
def main():
    file = 'multiple_new_trains/8b_2s_3et_3nt_63t_146'  # no .py, base folder: common_data/networks
    directory = 'common_data/networks/multiple_new_trains'

    run_on_file(filepath=file, models=['ten_it', 'mip_it', 'mip_gl'], plot_timetable=1)
    # run_on_folder(directory=directory, models=['ten_it', 'mip_it', 'mip_gl'],
    #              filename_filter='10b', plot_timetable=1)
    # ten_iteratively(filepath=file, plot_timetable=1, draw_tens=1, drawing_timehorizon=(60, 70), print_solution=0)
    # mip_iteratively(filepath=file, plot_timetable=0, print_solution=2)


if __name__ == '__main__':
    main()
