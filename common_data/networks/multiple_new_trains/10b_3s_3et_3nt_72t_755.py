data = {'nodes': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 'start_node': '0', 'end_node': '9',
        'edges': [('0', '1'), ('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7'), ('7', '8'),
                  ('8', '9')],
        'nodes_labels': {'0': 'switch', '1': 'station', '2': 'switch', '3': 'switch', '4': 'station', '5': 'switch',
                         '6': 'switch', '7': 'station', '8': 'switch', '9': 'signal'},
        'capacities': {('0', '0'): 1, ('0', '1'): 1, ('1', '1'): 1, ('1', '2'): 1, ('2', '2'): 1, ('2', '3'): 1,
                       ('3', '3'): 1, ('3', '4'): 2, ('4', '4'): 2, ('4', '5'): 2, ('5', '5'): 1, ('5', '6'): 1,
                       ('6', '6'): 1, ('6', '7'): 1, ('7', '7'): 1, ('7', '8'): 1, ('8', '8'): 1, ('8', '9'): 1},
        'existing_trains': {'ICE_0': {'start': 1,
                                      'traveltimes': {('0', '0'): 1, ('1', '1'): 1, ('2', '2'): 1, ('3', '3'): 1,
                                                      ('6', '6'): 1, ('7', '7'): 1, ('8', '8'): 1, ('0', '1'): 1,
                                                      ('1', '2'): 1, ('2', '3'): 1, ('5', '6'): 1, ('6', '7'): 1,
                                                      ('7', '8'): 1, ('8', '9'): 1, ('3', '4'): 1, ('4', '4'): 10,
                                                      ('4', '5'): 1, ('5', '5'): 1},
                                      'arrival_times': {'1': 3, '4': 9, '7': 24, '9': 28},
                                      'departure_times': {'1': 4, '4': 19, '7': 25}}, 'RE_0': {'start': 11,
                                                                                               'traveltimes': {
                                                                                                   ('0', '0'): 1,
                                                                                                   ('1', '1'): 2,
                                                                                                   ('2', '2'): 2,
                                                                                                   ('3', '3'): 1,
                                                                                                   ('6', '6'): 2,
                                                                                                   ('7', '7'): 2,
                                                                                                   ('8', '8'): 1,
                                                                                                   ('0', '1'): 1,
                                                                                                   ('1', '2'): 1,
                                                                                                   ('2', '3'): 1,
                                                                                                   ('5', '6'): 2,
                                                                                                   ('6', '7'): 2,
                                                                                                   ('7', '8'): 1,
                                                                                                   ('8', '9'): 1,
                                                                                                   ('3', '4'): 1,
                                                                                                   ('4', '4'): 4,
                                                                                                   ('4', '5'): 2,
                                                                                                   ('5', '5'): 2},
                                                                                               'arrival_times': {
                                                                                                   '1': 13, '4': 21,
                                                                                                   '7': 35, '9': 40},
                                                                                               'departure_times': {
                                                                                                   '1': 15, '4': 25,
                                                                                                   '7': 37}},
                            'RE_1': {'start': 31,
                                     'traveltimes': {('0', '0'): 1, ('1', '1'): 2, ('2', '2'): 2, ('3', '3'): 1,
                                                     ('6', '6'): 2, ('7', '7'): 2, ('8', '8'): 1, ('0', '1'): 1,
                                                     ('1', '2'): 1, ('2', '3'): 1, ('5', '6'): 2, ('6', '7'): 2,
                                                     ('7', '8'): 1, ('8', '9'): 1, ('3', '4'): 1, ('4', '4'): 4,
                                                     ('4', '5'): 2, ('5', '5'): 2},
                                     'arrival_times': {'1': 33, '4': 41, '7': 55, '9': 60},
                                     'departure_times': {'1': 35, '4': 45, '7': 57}}}, 'new_trains_traveltimes': {
        'new_train_s_0': {'start': 5,
                          'traveltimes': {('0', '0'): 1, ('0', '1'): 1, ('1', '1'): 2, ('1', '2'): 1, ('2', '2'): 2,
                                          ('2', '3'): 1, ('3', '3'): 1, ('3', '4'): 1, ('4', '4'): 4, ('4', '5'): 2,
                                          ('5', '5'): 2, ('5', '6'): 2, ('6', '6'): 2, ('6', '7'): 2, ('7', '7'): 2,
                                          ('7', '8'): 1, ('8', '8'): 1, ('8', '9'): 1},
                          'arrival_times': {'1': 7, '4': 15, '7': 29, '9': 34},
                          'departure_times': {'1': 9, '4': 19, '7': 31}}, 'new_train_s_1': {'start': 15,
                                                                                            'traveltimes': {
                                                                                                ('0', '0'): 1,
                                                                                                ('0', '1'): 1,
                                                                                                ('1', '1'): 2,
                                                                                                ('1', '2'): 1,
                                                                                                ('2', '2'): 2,
                                                                                                ('2', '3'): 1,
                                                                                                ('3', '3'): 1,
                                                                                                ('3', '4'): 1,
                                                                                                ('4', '4'): 4,
                                                                                                ('4', '5'): 2,
                                                                                                ('5', '5'): 2,
                                                                                                ('5', '6'): 2,
                                                                                                ('6', '6'): 2,
                                                                                                ('6', '7'): 2,
                                                                                                ('7', '7'): 2,
                                                                                                ('7', '8'): 1,
                                                                                                ('8', '8'): 1,
                                                                                                ('8', '9'): 1},
                                                                                            'arrival_times': {'1': 17,
                                                                                                              '4': 25,
                                                                                                              '7': 39,
                                                                                                              '9': 44},
                                                                                            'departure_times': {'1': 19,
                                                                                                                '4': 29,
                                                                                                                '7': 41}},
        'new_train_s_2': {'start': 25,
                          'traveltimes': {('0', '0'): 1, ('0', '1'): 1, ('1', '1'): 2, ('1', '2'): 1, ('2', '2'): 2,
                                          ('2', '3'): 1, ('3', '3'): 1, ('3', '4'): 1, ('4', '4'): 4, ('4', '5'): 2,
                                          ('5', '5'): 2, ('5', '6'): 2, ('6', '6'): 2, ('6', '7'): 2, ('7', '7'): 2,
                                          ('7', '8'): 1, ('8', '8'): 1, ('8', '9'): 1},
                          'arrival_times': {'1': 27, '4': 35, '7': 49, '9': 54},
                          'departure_times': {'1': 29, '4': 39, '7': 51}}}, 'timehorizon': 72}
