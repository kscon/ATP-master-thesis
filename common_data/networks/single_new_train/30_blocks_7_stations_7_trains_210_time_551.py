data = {
    'nodes': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
              '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29'], 'start_node': '0', 'end_node': '29',
    'edges': [('0', '1'), ('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7'), ('7', '8'),
              ('8', '9'), ('9', '10'), ('10', '11'), ('11', '12'), ('12', '13'), ('13', '14'), ('14', '15'),
              ('15', '16'), ('16', '17'), ('17', '18'), ('18', '19'), ('19', '20'), ('20', '21'), ('21', '22'),
              ('22', '23'), ('23', '24'), ('24', '25'), ('25', '26'), ('26', '27'), ('27', '28'), ('28', '29')],
    'nodes_labels': {'0': 'signal', '1': 'switch', '2': 'station', '3': 'switch', '4': 'switch', '5': 'station',
                     '6': 'switch', '7': 'signal', '8': 'signal', '9': 'switch', '10': 'station', '11': 'switch',
                     '12': 'switch', '13': 'station', '14': 'switch', '15': 'signal', '16': 'signal', '17': 'signal',
                     '18': 'switch', '19': 'station', '20': 'switch', '21': 'switch', '22': 'station', '23': 'switch',
                     '24': 'switch', '25': 'station', '26': 'switch', '27': 'signal', '28': 'signal', '29': 'signal'},
    'capacities': {('0', '1'): 1, ('1', '1'): 1, ('1', '2'): 2, ('2', '2'): 2, ('2', '3'): 2, ('3', '3'): 1,
                   ('3', '4'): 1, ('4', '4'): 1, ('4', '5'): 1, ('5', '5'): 1, ('5', '6'): 1, ('6', '6'): 1,
                   ('6', '7'): 1, ('7', '8'): 1, ('8', '9'): 1, ('9', '9'): 1, ('9', '10'): 1, ('10', '10'): 1,
                   ('10', '11'): 1, ('11', '11'): 1, ('11', '12'): 1, ('12', '12'): 1, ('12', '13'): 4, ('13', '13'): 4,
                   ('13', '14'): 4, ('14', '14'): 1, ('14', '15'): 1, ('15', '16'): 1, ('16', '17'): 1, ('17', '18'): 1,
                   ('18', '18'): 1, ('18', '19'): 2, ('19', '19'): 2, ('19', '20'): 2, ('20', '20'): 1, ('20', '21'): 1,
                   ('21', '21'): 1, ('21', '22'): 1, ('22', '22'): 1, ('22', '23'): 1, ('23', '23'): 1, ('23', '24'): 1,
                   ('24', '24'): 1, ('24', '25'): 2, ('25', '25'): 2, ('25', '26'): 2, ('26', '26'): 1, ('26', '27'): 1,
                   ('27', '28'): 1, ('28', '29'): 1}, 'existing_trains': {
        'ICE_0': {'start': 1,
                  'traveltimes': {('0', '1'): 1,
                                  ('1', '1'): 1,
                                  ('2', '2'): 1,
                                  ('3', '3'): 1,
                                  ('4', '4'): 1,
                                  ('5', '5'): 1,
                                  ('6', '6'): 1,
                                  ('7', '8'): 1,
                                  ('8', '9'): 1,
                                  ('9', '9'): 1,
                                  ('10', '10'): 1,
                                  ('11', '11'): 1,
                                  ('12', '12'): 1,
                                  ('15', '16'): 1,
                                  ('16', '17'): 1,
                                  ('17', '18'): 1,
                                  ('18', '18'): 1,
                                  ('19', '19'): 1,
                                  ('20', '20'): 1,
                                  ('21', '21'): 1,
                                  ('22', '22'): 1,
                                  ('23', '23'): 1,
                                  ('24', '24'): 1,
                                  ('27', '28'): 1,
                                  ('28', '29'): 1,
                                  ('1', '2'): 1,
                                  ('2', '3'): 1,
                                  ('3', '4'): 1,
                                  ('4', '5'): 1,
                                  ('5', '6'): 1,
                                  ('6', '7'): 1,
                                  ('9', '10'): 1,
                                  ('10', '11'): 1,
                                  ('11', '12'): 1,
                                  ('14', '15'): 1,
                                  ('18', '19'): 1,
                                  ('19', '20'): 1,
                                  ('20', '21'): 1,
                                  ('21', '22'): 1,
                                  ('22', '23'): 1,
                                  ('23', '24'): 1,
                                  ('26', '27'): 1,
                                  ('12', '13'): 1,
                                  ('13', '13'): 10,
                                  ('13', '14'): 1,
                                  ('14', '14'): 1,
                                  ('24', '25'): 1,
                                  ('25', '25'): 10,
                                  ('25', '26'): 1,
                                  ('26', '26'): 1},
                  'arrival_times': {'2': 4, '5': 10,
                                    '10': 18,
                                    '13': 24,
                                    '19': 42,
                                    '22': 48,
                                    '25': 54,
                                    '29': 69},
                  'departure_times': {'2': 5, '5': 11,
                                      '10': 19,
                                      '13': 34,
                                      '19': 43,
                                      '22': 49,
                                      '25': 64}},
        'ICE_1': {'start': 21,
                  'traveltimes': {('0', '1'): 1,
                                  ('1', '1'): 1,
                                  ('2', '2'): 1,
                                  ('3', '3'): 1,
                                  ('4', '4'): 1,
                                  ('5', '5'): 1,
                                  ('6', '6'): 1,
                                  ('7', '8'): 1,
                                  ('8', '9'): 1,
                                  ('9', '9'): 1,
                                  ('10', '10'): 1,
                                  ('11', '11'): 1,
                                  ('12', '12'): 1,
                                  ('13', '13'): 10,
                                  ('14', '14'): 1,
                                  ('15', '16'): 1,
                                  ('16', '17'): 1,
                                  ('17', '18'): 1,
                                  ('18', '18'): 1,
                                  ('19', '19'): 1,
                                  ('20', '20'): 1,
                                  ('21', '21'): 1,
                                  ('22', '22'): 1,
                                  ('23', '23'): 1,
                                  ('24', '24'): 1,
                                  ('25', '25'): 10,
                                  ('26', '26'): 1,
                                  ('27', '28'): 1,
                                  ('28', '29'): 1,
                                  ('1', '2'): 1,
                                  ('2', '3'): 1,
                                  ('3', '4'): 1,
                                  ('4', '5'): 1,
                                  ('5', '6'): 1,
                                  ('6', '7'): 1,
                                  ('9', '10'): 5,
                                  ('10', '11'): 1,
                                  ('11', '12'): 1,
                                  ('12', '13'): 1,
                                  ('13', '14'): 1,
                                  ('14', '15'): 1,
                                  ('18', '19'): 1,
                                  ('19', '20'): 1,
                                  ('20', '21'): 1,
                                  ('21', '22'): 1,
                                  ('22', '23'): 1,
                                  ('23', '24'): 1,
                                  ('24', '25'): 1,
                                  ('25', '26'): 1,
                                  ('26', '27'): 1},
                  'arrival_times': {'2': 24, '5': 30,
                                    '10': 42,
                                    '13': 48,
                                    '19': 66,
                                    '22': 72,
                                    '25': 78,
                                    '29': 93},
                  'departure_times': {'2': 25,
                                      '5': 31,
                                      '10': 43,
                                      '13': 58,
                                      '19': 67,
                                      '22': 73,
                                      '25': 88}},
        'RE_0': {'start': 11,
                 'traveltimes': {('0', '1'): 2,
                                 ('1', '1'): 1,
                                 ('4', '4'): 1,
                                 ('5', '5'): 2,
                                 ('6', '6'): 1,
                                 ('7', '8'): 2,
                                 ('8', '9'): 2,
                                 ('9', '9'): 1,
                                 ('10', '10'): 2,
                                 ('11', '11'): 1,
                                 ('12', '12'): 2,
                                 ('15', '16'): 1,
                                 ('16', '17'): 2,
                                 ('17', '18'): 1,
                                 ('18', '18'): 2,
                                 ('21', '21'): 1,
                                 ('22', '22'): 2,
                                 ('23', '23'): 2,
                                 ('24', '24'): 2,
                                 ('27', '28'): 2,
                                 ('28', '29'): 1,
                                 ('3', '4'): 2,
                                 ('4', '5'): 1,
                                 ('5', '6'): 2,
                                 ('6', '7'): 1,
                                 ('9', '10'): 2,
                                 ('10', '11'): 2,
                                 ('11', '12'): 2,
                                 ('14', '15'): 1,
                                 ('20', '21'): 2,
                                 ('21', '22'): 1,
                                 ('22', '23'): 2,
                                 ('23', '24'): 2,
                                 ('26', '27'): 2,
                                 ('1', '2'): 1,
                                 ('2', '2'): 2,
                                 ('12', '13'): 2,
                                 ('13', '13'): 4,
                                 ('13', '14'): 2,
                                 ('14', '14'): 2,
                                 ('18', '19'): 1,
                                 ('19', '19'): 2,
                                 ('19', '20'): 3,
                                 ('20', '20'): 1,
                                 ('2', '3'): 2,
                                 ('3', '3'): 1,
                                 ('24', '25'): 2,
                                 ('25', '25'): 4,
                                 ('25', '26'): 1,
                                 ('26', '26'): 1},
                 'arrival_times': {'2': 15, '5': 24,
                                   '10': 37, '13': 48,
                                   '19': 64, '22': 74,
                                   '25': 86,
                                   '29': 97},
                 'departure_times': {'2': 17, '5': 26,
                                     '10': 39,
                                     '13': 52,
                                     '19': 66,
                                     '22': 76,
                                     '25': 90}},
        'RE_1': {'start': 31,
                 'traveltimes': {('0', '1'): 2,
                                 ('1', '1'): 1,
                                 ('2', '2'): 2,
                                 ('3', '3'): 1,
                                 ('4', '4'): 1,
                                 ('5', '5'): 2,
                                 ('6', '6'): 1,
                                 ('7', '8'): 2,
                                 ('8', '9'): 2,
                                 ('9', '9'): 1,
                                 ('10', '10'): 2,
                                 ('11', '11'): 1,
                                 ('12', '12'): 2,
                                 ('15', '16'): 1,
                                 ('16', '17'): 2,
                                 ('17', '18'): 1,
                                 ('18', '18'): 2,
                                 ('19', '19'): 2,
                                 ('20', '20'): 1,
                                 ('21', '21'): 1,
                                 ('22', '22'): 2,
                                 ('23', '23'): 2,
                                 ('24', '24'): 2,
                                 ('25', '25'): 4,
                                 ('26', '26'): 1,
                                 ('27', '28'): 2,
                                 ('28', '29'): 1,
                                 ('1', '2'): 1,
                                 ('2', '3'): 2,
                                 ('3', '4'): 2,
                                 ('4', '5'): 1,
                                 ('5', '6'): 2,
                                 ('6', '7'): 1,
                                 ('9', '10'): 2,
                                 ('10', '11'): 2,
                                 ('11', '12'): 2,
                                 ('14', '15'): 1,
                                 ('18', '19'): 1,
                                 ('19', '20'): 1,
                                 ('20', '21'): 2,
                                 ('21', '22'): 1,
                                 ('22', '23'): 2,
                                 ('23', '24'): 2,
                                 ('24', '25'): 2,
                                 ('25', '26'): 1,
                                 ('26', '27'): 2,
                                 ('12', '13'): 2,
                                 ('13', '13'): 4,
                                 ('13', '14'): 2,
                                 ('14', '14'): 2},
                 'arrival_times': {'2': 35, '5': 44,
                                   '10': 57, '13': 68,
                                   '19': 84, '22': 92,
                                   '25': 104,
                                   '29': 115},
                 'departure_times': {'2': 37, '5': 46,
                                     '10': 59,
                                     '13': 72,
                                     '19': 86,
                                     '22': 94,
                                     '25': 108}},
        'RE_2': {'start': 51,
                 'traveltimes': {('0', '1'): 2,
                                 ('1', '1'): 1,
                                 ('2', '2'): 2,
                                 ('3', '3'): 1,
                                 ('4', '4'): 1,
                                 ('5', '5'): 2,
                                 ('6', '6'): 1,
                                 ('7', '8'): 2,
                                 ('8', '9'): 2,
                                 ('9', '9'): 1,
                                 ('10', '10'): 2,
                                 ('11', '11'): 1,
                                 ('12', '12'): 2,
                                 ('15', '16'): 1,
                                 ('16', '17'): 2,
                                 ('17', '18'): 1,
                                 ('18', '18'): 2,
                                 ('21', '21'): 1,
                                 ('22', '22'): 2,
                                 ('23', '23'): 2,
                                 ('24', '24'): 2,
                                 ('25', '25'): 4,
                                 ('26', '26'): 1,
                                 ('27', '28'): 2,
                                 ('28', '29'): 1,
                                 ('1', '2'): 1,
                                 ('2', '3'): 2,
                                 ('3', '4'): 2,
                                 ('4', '5'): 1,
                                 ('5', '6'): 2,
                                 ('6', '7'): 1,
                                 ('9', '10'): 2,
                                 ('10', '11'): 2,
                                 ('11', '12'): 2,
                                 ('14', '15'): 1,
                                 ('20', '21'): 2,
                                 ('21', '22'): 1,
                                 ('22', '23'): 2,
                                 ('23', '24'): 2,
                                 ('24', '25'): 2,
                                 ('25', '26'): 1,
                                 ('26', '27'): 2,
                                 ('12', '13'): 2,
                                 ('13', '13'): 4,
                                 ('13', '14'): 2,
                                 ('14', '14'): 2,
                                 ('18', '19'): 1,
                                 ('19', '19'): 2,
                                 ('19', '20'): 1,
                                 ('20', '20'): 1},
                 'arrival_times': {'2': 55, '5': 64,
                                   '10': 77, '13': 88,
                                   '19': 104,
                                   '22': 112,
                                   '25': 124,
                                   '29': 135},
                 'departure_times': {'2': 57, '5': 66,
                                     '10': 79,
                                     '13': 92,
                                     '19': 106,
                                     '22': 114,
                                     '25': 128}},
        'RE_3': {'start': 71,
                 'traveltimes': {('0', '1'): 2,
                                 ('1', '1'): 1,
                                 ('2', '2'): 2,
                                 ('3', '3'): 1,
                                 ('4', '4'): 1,
                                 ('5', '5'): 2,
                                 ('6', '6'): 1,
                                 ('7', '8'): 2,
                                 ('8', '9'): 2,
                                 ('9', '9'): 1,
                                 ('10', '10'): 2,
                                 ('11', '11'): 1,
                                 ('12', '12'): 2,
                                 ('13', '13'): 4,
                                 ('14', '14'): 2,
                                 ('15', '16'): 1,
                                 ('16', '17'): 2,
                                 ('17', '18'): 1,
                                 ('18', '18'): 2,
                                 ('19', '19'): 2,
                                 ('20', '20'): 1,
                                 ('21', '21'): 1,
                                 ('22', '22'): 2,
                                 ('23', '23'): 2,
                                 ('24', '24'): 2,
                                 ('27', '28'): 2,
                                 ('28', '29'): 1,
                                 ('1', '2'): 1,
                                 ('2', '3'): 2,
                                 ('3', '4'): 2,
                                 ('4', '5'): 1,
                                 ('5', '6'): 2,
                                 ('6', '7'): 1,
                                 ('9', '10'): 2,
                                 ('10', '11'): 2,
                                 ('11', '12'): 2,
                                 ('12', '13'): 2,
                                 ('13', '14'): 2,
                                 ('14', '15'): 1,
                                 ('18', '19'): 1,
                                 ('19', '20'): 1,
                                 ('20', '21'): 2,
                                 ('21', '22'): 1,
                                 ('22', '23'): 2,
                                 ('23', '24'): 2,
                                 ('26', '27'): 2,
                                 ('24', '25'): 2,
                                 ('25', '25'): 4,
                                 ('25', '26'): 1,
                                 ('26', '26'): 1},
                 'arrival_times': {'2': 75, '5': 84,
                                   '10': 97,
                                   '13': 108,
                                   '19': 124,
                                   '22': 132,
                                   '25': 144,
                                   '29': 155},
                 'departure_times': {'2': 77, '5': 86,
                                     '10': 99,
                                     '13': 112,
                                     '19': 126,
                                     '22': 134,
                                     '25': 148}},
        'RE_4': {'start': 91,
                 'traveltimes': {('0', '1'): 2,
                                 ('1', '1'): 1,
                                 ('2', '2'): 2,
                                 ('3', '3'): 1,
                                 ('4', '4'): 1,
                                 ('5', '5'): 2,
                                 ('6', '6'): 1,
                                 ('7', '8'): 2,
                                 ('8', '9'): 2,
                                 ('9', '9'): 1,
                                 ('10', '10'): 2,
                                 ('11', '11'): 1,
                                 ('12', '12'): 2,
                                 ('13', '13'): 4,
                                 ('14', '14'): 2,
                                 ('15', '16'): 1,
                                 ('16', '17'): 2,
                                 ('17', '18'): 1,
                                 ('18', '18'): 2,
                                 ('19', '19'): 2,
                                 ('20', '20'): 1,
                                 ('21', '21'): 1,
                                 ('22', '22'): 2,
                                 ('23', '23'): 2,
                                 ('24', '24'): 2,
                                 ('25', '25'): 4,
                                 ('26', '26'): 1,
                                 ('27', '28'): 2,
                                 ('28', '29'): 1,
                                 ('1', '2'): 1,
                                 ('2', '3'): 2,
                                 ('3', '4'): 2,
                                 ('4', '5'): 1,
                                 ('5', '6'): 2,
                                 ('6', '7'): 1,
                                 ('9', '10'): 2,
                                 ('10', '11'): 2,
                                 ('11', '12'): 2,
                                 ('12', '13'): 2,
                                 ('13', '14'): 2,
                                 ('14', '15'): 1,
                                 ('18', '19'): 1,
                                 ('19', '20'): 1,
                                 ('20', '21'): 2,
                                 ('21', '22'): 1,
                                 ('22', '23'): 2,
                                 ('23', '24'): 2,
                                 ('24', '25'): 2,
                                 ('25', '26'): 1,
                                 ('26', '27'): 2},
                 'arrival_times': {'2': 95, '5': 104,
                                   '10': 117,
                                   '13': 128,
                                   '19': 144,
                                   '22': 152,
                                   '25': 164,
                                   '29': 175},
                 'departure_times': {'2': 97,
                                     '5': 106,
                                     '10': 119,
                                     '13': 132,
                                     '19': 146,
                                     '22': 154,
                                     '25': 168}}},
    'new_trains_traveltimes': {'new_train': {'start': 5,
                                             'traveltimes': {('0', '1'): 2, ('1', '1'): 1, ('1', '2'): 1, ('2', '2'): 2,
                                                             ('2', '3'): 2, ('3', '3'): 1, ('3', '4'): 2, ('4', '4'): 1,
                                                             ('4', '5'): 1, ('5', '5'): 2, ('5', '6'): 2, ('6', '6'): 1,
                                                             ('6', '7'): 1, ('7', '8'): 2, ('8', '9'): 2, ('9', '9'): 1,
                                                             ('9', '10'): 2, ('10', '10'): 2, ('10', '11'): 2,
                                                             ('11', '11'): 1, ('11', '12'): 2, ('12', '12'): 2,
                                                             ('12', '13'): 2, ('13', '13'): 4, ('13', '14'): 2,
                                                             ('14', '14'): 2, ('14', '15'): 1, ('15', '16'): 1,
                                                             ('16', '17'): 2, ('17', '18'): 1, ('18', '18'): 2,
                                                             ('18', '19'): 1, ('19', '19'): 2, ('19', '20'): 1,
                                                             ('20', '20'): 1, ('20', '21'): 2, ('21', '21'): 1,
                                                             ('21', '22'): 1, ('22', '22'): 2, ('22', '23'): 2,
                                                             ('23', '23'): 2, ('23', '24'): 2, ('24', '24'): 2,
                                                             ('24', '25'): 2, ('25', '25'): 4, ('25', '26'): 1,
                                                             ('26', '26'): 1, ('26', '27'): 2, ('27', '28'): 2,
                                                             ('28', '29'): 1},
                                             'arrival_times': {'2': 9, '5': 18, '10': 31, '13': 42, '19': 58, '22': 66,
                                                               '25': 78, '29': 89},
                                             'departure_times': {'2': 11, '5': 20, '10': 33, '13': 46, '19': 60,
                                                                 '22': 68, '25': 82}}}, 'timehorizon': 210}
