data = {'nodes': ['0', '1', '2', '3', '4', '5', '6', '7'], 'start_node': '0', 'end_node': '7',
        'edges': [('0', '1'), ('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7')],
        'nodes_labels': {'0': 'signal', '1': 'switch', '2': 'station', '3': 'switch', '4': 'switch', '5': 'station',
                         '6': 'switch', '7': 'signal'},
        'capacities': {('0', '1'): 1, ('1', '1'): 1, ('1', '2'): 1, ('2', '2'): 1, ('2', '3'): 1, ('3', '3'): 1,
                       ('3', '4'): 1, ('4', '4'): 1, ('4', '5'): 2, ('5', '5'): 2, ('5', '6'): 2, ('6', '6'): 1,
                       ('6', '7'): 1}, 'existing_trains': {'ICE_0': {'start': 1,
                                                                     'traveltimes': {('0', '1'): 1, ('1', '1'): 1,
                                                                                     ('2', '2'): 1, ('3', '3'): 1,
                                                                                     ('4', '4'): 1, ('1', '2'): 1,
                                                                                     ('2', '3'): 1, ('3', '4'): 1,
                                                                                     ('6', '7'): 1, ('4', '5'): 1,
                                                                                     ('5', '5'): 10, ('5', '6'): 1,
                                                                                     ('6', '6'): 1},
                                                                     'arrival_times': {'2': 4, '5': 10, '7': 23},
                                                                     'departure_times': {'2': 5, '5': 20}},
                                                           'RE_0': {'start': 11,
                                                                    'traveltimes': {('0', '1'): 2, ('1', '1'): 2,
                                                                                    ('2', '2'): 2, ('3', '3'): 2,
                                                                                    ('4', '4'): 1, ('1', '2'): 1,
                                                                                    ('2', '3'): 2, ('3', '4'): 1,
                                                                                    ('6', '7'): 1, ('4', '5'): 2,
                                                                                    ('5', '5'): 4, ('5', '6'): 1,
                                                                                    ('6', '6'): 1},
                                                                    'arrival_times': {'2': 16, '5': 26, '7': 33},
                                                                    'departure_times': {'2': 18, '5': 30}},
                                                           'RE_1': {'start': 31,
                                                                    'traveltimes': {('0', '1'): 2, ('1', '1'): 2,
                                                                                    ('2', '2'): 2, ('3', '3'): 2,
                                                                                    ('4', '4'): 1, ('1', '2'): 1,
                                                                                    ('2', '3'): 2, ('3', '4'): 1,
                                                                                    ('6', '7'): 1, ('4', '5'): 2,
                                                                                    ('5', '5'): 4, ('5', '6'): 1,
                                                                                    ('6', '6'): 1},
                                                                    'arrival_times': {'2': 36, '5': 46, '7': 53},
                                                                    'departure_times': {'2': 38, '5': 50}}},
        'new_trains_traveltimes': {'new_train_s_0': {'start': 5,
                                                     'traveltimes': {('0', '1'): 2, ('1', '1'): 2, ('1', '2'): 1,
                                                                     ('2', '2'): 2, ('2', '3'): 2, ('3', '3'): 2,
                                                                     ('3', '4'): 1, ('4', '4'): 1, ('4', '5'): 2,
                                                                     ('5', '5'): 4, ('5', '6'): 1, ('6', '6'): 1,
                                                                     ('6', '7'): 1},
                                                     'arrival_times': {'2': 10, '5': 20, '7': 27},
                                                     'departure_times': {'2': 12, '5': 24}},
                                   'new_train_f_1': {'start': 15,
                                                     'traveltimes': {('0', '1'): 1, ('1', '1'): 1, ('1', '2'): 1,
                                                                     ('2', '2'): 1, ('2', '3'): 1, ('3', '3'): 1,
                                                                     ('3', '4'): 1, ('4', '4'): 1, ('4', '5'): 1,
                                                                     ('5', '5'): 10, ('5', '6'): 1, ('6', '6'): 1,
                                                                     ('6', '7'): 1},
                                                     'arrival_times': {'2': 18, '5': 24, '7': 37},
                                                     'departure_times': {'2': 19, '5': 34}},
                                   'new_train_f_2': {'start': 25,
                                                     'traveltimes': {('0', '1'): 1, ('1', '1'): 1, ('1', '2'): 1,
                                                                     ('2', '2'): 1, ('2', '3'): 1, ('3', '3'): 1,
                                                                     ('3', '4'): 1, ('4', '4'): 1, ('4', '5'): 1,
                                                                     ('5', '5'): 10, ('5', '6'): 1, ('6', '6'): 1,
                                                                     ('6', '7'): 1},
                                                     'arrival_times': {'2': 28, '5': 34, '7': 47},
                                                     'departure_times': {'2': 29, '5': 44}}}, 'timehorizon': 63}