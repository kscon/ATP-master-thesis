import itertools
import os
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def render_timetable(data):
    timetable = data['timetable']
    blocks = [l[0] for l in data['layers']]
    trains_list = list(timetable.keys())
    arrival_chart = {}
    max_time = 0

    for r in trains_list:
        arrival_chart[r] = {}
        counter_time = timetable[r]['start']
        for b in blocks:
            arrival_chart[r][b] = counter_time
            block_pair = None
            if '#' not in b:
                block_pair = [(sb, tb) for (sb, tb) in timetable[r]['traveltimes'].keys() if sb == b and tb == sb]
                if len(block_pair) != 1:
                    block_pair = [(sb, tb) for (sb, tb) in timetable[r]['traveltimes'].keys() if sb == b and tb != sb]
            elif '#' in b:
                block_pair = [(sb, tb) for (sb, tb) in timetable[r]['traveltimes'].keys()
                              if sb == b.strip('#') and sb != tb]
            if len(block_pair) == 1:
                counter_time += timetable[r]['traveltimes'][block_pair[0]]
                max_time = max(max_time, counter_time)
            elif b != blocks[-1]:
                assert False

    df = pd.DataFrame({'blocks': blocks})
    df = df.set_index('blocks')
    df = df.join(pd.DataFrame(
        {t: '' for t in range(max_time + 1)}, index=df.index
    ))

    # idea: in timing chart, save a dataframe of block/time and a number in that field, if train x is currently in it
    for sb, eb in itertools.pairwise(blocks):
        for ac in arrival_chart:
            if sb in arrival_chart[ac].keys() and eb in arrival_chart[ac].keys():
                arrival_time = arrival_chart[ac][sb]
                departure_time = arrival_chart[ac][eb]
                for tt in range(arrival_time, departure_time):
                    df.loc[sb, tt] += ac + ' '
                if eb == blocks[-1]:
                    df.loc[eb, departure_time] += ac + '_'

    filename = data['filepath'].split('/')[-1]
    folder = 'output/' + data['filepath'] + '/'
    full_file_string = ''
    if data['model'] == 'mip':
        full_file_string = 'timetable_' + data['model'] + '_' + filename + '_' + \
                  data['model_mode'] + '_' + str(data['iteration_counter'])
    else:
        full_file_string = 'timetable_' + data['model'] + '_' + filename + '_' + \
                  str(data['iteration_counter'])

    if not os.path.exists(folder):
        os.makedirs(folder)

    df.to_csv(folder + full_file_string + '.csv', sep=';')

    df_transposed = df.transpose()
    # plot dataframe
    # figsize=(10, 6)
    # 10 = x* 60, 18 = x*105
    # 6 = y*20, 10 = y*32
    fig, ax = plt.subplots(figsize=(int(max_time*0.17), int(len(blocks)*0.3)))
    # color dict
    color_dict = dict(zip(trains_list, [i for i in range(len(trains_list))]))
    y_dict = dict(zip(blocks, [i for i in range(len(blocks))]))  # x_dict is given as timehorizon

    for bb in blocks:
        col_T = df_transposed[bb]
        block_data = list(zip(range(max_time), col_T))

        for t in trains_list:
            block_data_train_wise = [(tt, 1) for (tt, s) in block_data if t in s]
            ax.broken_barh(block_data_train_wise, (y_dict[bb], 1), facecolor=plt.cm.tab20(color_dict[t]))

    ax.set_xlabel('time (min)')
    ax.set_ylabel('blocks')
    ax.set_xticks([5 * i for i in range(max_time // 5)] + [max_time],
                  labels=[str(5 * i) for i in range(max_time // 5)] + [str(max_time)])
    ax.set_yticks([i for i in range(len(blocks))], labels=blocks)  # Modify y-axis tick labels
    ax.set_title('Timetable of file: ' + filename + ' - ' + data['model'] + ' - ' + ' - New Train Insertion It. '
                 + str(data['iteration_counter']))
    ax.grid(True)  # Make grid lines visible

    legend_elements = [mpl.patches.Patch(facecolor=plt.cm.tab20(color_dict[t]), label=t) for t in trains_list]
    #ax.legend(handles=legend_elements, bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)
    ax.legend(handles=legend_elements, loc='lower right')
    # plt.show()

    plt.savefig(folder + full_file_string + '.png', format='png', bbox_inches='tight')
    plt.savefig(folder + full_file_string+ '.pdf', format='pdf', bbox_inches='tight')
    plt.close()
