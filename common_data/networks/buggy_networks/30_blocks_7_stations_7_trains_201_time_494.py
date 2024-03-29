data = {
    'nodes': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
              '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29'], 'start_node': '0', 'end_node': '29',
    'edges': [('0', '1'), ('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7'), ('7', '8'),
              ('8', '9'), ('9', '10'), ('10', '11'), ('11', '12'), ('12', '13'), ('13', '14'), ('14', '15'),
              ('15', '16'), ('16', '17'), ('17', '18'), ('18', '19'), ('19', '20'), ('20', '21'), ('21', '22'),
              ('22', '23'), ('23', '24'), ('24', '25'), ('25', '26'), ('26', '27'), ('27', '28'), ('28', '29')],
    'nodes_labels': {'0': 'signal', '1': 'signal', '2': 'signal', '3': 'signal', '4': 'switch', '5': 'station',
                     '6': 'switch', '7': 'signal', '8': 'switch', '9': 'station', '10': 'switch', '11': 'switch',
                     '12': 'station', '13': 'switch', '14': 'switch', '15': 'station', '16': 'switch', '17': 'signal',
                     '18': 'switch', '19': 'station', '20': 'switch', '21': 'signal', '22': 'signal', '23': 'switch',
                     '24': 'station', '25': 'switch', '26': 'switch', '27': 'station', '28': 'switch', '29': 'signal'},
    'capacities': {('0', '1'): 1, ('1', '2'): 1, ('2', '3'): 1, ('3', '4'): 1, ('4', '4'): 1, ('4', '5'): 2,
                   ('5', '5'): 2, ('5', '6'): 2, ('6', '6'): 1, ('6', '7'): 1, ('7', '8'): 1, ('8', '8'): 1,
                   ('8', '9'): 1, ('9', '9'): 1, ('9', '10'): 1, ('10', '10'): 1, ('10', '11'): 1, ('11', '11'): 1,
                   ('11', '12'): 3, ('12', '12'): 3, ('12', '13'): 3, ('13', '13'): 1, ('13', '14'): 1, ('14', '14'): 1,
                   ('14', '15'): 1, ('15', '15'): 1, ('15', '16'): 1, ('16', '16'): 1, ('16', '17'): 1, ('17', '18'): 1,
                   ('18', '18'): 1, ('18', '19'): 2, ('19', '19'): 2, ('19', '20'): 2, ('20', '20'): 1, ('20', '21'): 1,
                   ('21', '22'): 1, ('22', '23'): 1, ('23', '23'): 1, ('23', '24'): 1, ('24', '24'): 1, ('24', '25'): 1,
                   ('25', '25'): 1, ('25', '26'): 1, ('26', '26'): 1, ('26', '27'): 3, ('27', '27'): 3, ('27', '28'): 3,
                   ('28', '28'): 1, ('28', '29'): 1},
    'existing_trains': {
        'ICE_0': {'start': 1,
                  'traveltimes': {('0', '1'): 1,
                                  ('1', '2'): 1,
                                  ('2', '3'): 1,
                                  ('3', '4'): 1,
                                  ('4', '4'): 1,
                                  ('7', '8'): 1,
                                  ('8', '8'): 1,
                                  ('9', '9'): 1,
                                  ('10', '10'): 1,
                                  ('11', '11'): 1,
                                  ('14', '14'): 1,
                                  ('15', '15'): 1,
                                  ('16', '16'): 1,
                                  ('17', '18'): 1,
                                  ('18', '18'): 1,
                                  ('19', '19'): 1,
                                  ('20', '20'): 1,
                                  ('21', '22'): 1,
                                  ('22', '23'): 1,
                                  ('23', '23'): 1,
                                  ('24', '24'): 1,
                                  ('25', '25'): 1,
                                  ('26', '26'): 1,
                                  ('27', '27'): 10,
                                  ('28', '28'): 1,
                                  ('6', '7'): 1,
                                  ('8', '9'): 1,
                                  ('9', '10'): 1,
                                  ('10', '11'): 1,
                                  ('13', '14'): 1,
                                  ('14', '15'): 1,
                                  ('15', '16'): 1,
                                  ('16', '17'): 1,
                                  ('18', '19'): 1,
                                  ('19', '20'): 1,
                                  ('20', '21'): 1,
                                  ('23', '24'): 1,
                                  ('24', '25'): 1,
                                  ('25', '26'): 1,
                                  ('26', '27'): 1,
                                  ('27', '28'): 1,
                                  ('28', '29'): 1,
                                  ('11', '12'): 1,
                                  ('12', '12'): 10,
                                  ('12', '13'): 1,
                                  ('13', '13'): 1,
                                  ('4', '5'): 1,
                                  ('5', '5'): 1,
                                  ('5', '6'): 1,
                                  ('6', '6'): 1},
                  'arrival_times': {'12': 7, '15': 22,
                                    '19': 29,
                                    '24': 38,
                                    '27': 44,
                                    '29': 57, '5': 60,
                                    '9': 68},
                  'departure_times': {'12': 17,
                                      '15': 23,
                                      '19': 30,
                                      '24': 39,
                                      '27': 54,
                                      '5': 61,
                                      '9': 69}},
        'ICE_1': {'start': 21,
                  'traveltimes': {('0', '1'): 1,
                                  ('1', '2'): 1,
                                  ('2', '3'): 1,
                                  ('3', '4'): 1,
                                  ('4', '4'): 1,
                                  ('7', '8'): 1,
                                  ('8', '8'): 1,
                                  ('9', '9'): 2,
                                  ('10', '10'): 1,
                                  ('11', '11'): 1,
                                  ('12', '12'): 10,
                                  ('13', '13'): 1,
                                  ('14', '14'): 1,
                                  ('15', '15'): 1,
                                  ('16', '16'): 1,
                                  ('17', '18'): 1,
                                  ('18', '18'): 1,
                                  ('19', '19'): 1,
                                  ('20', '20'): 1,
                                  ('21', '22'): 1,
                                  ('22', '23'): 1,
                                  ('23', '23'): 1,
                                  ('24', '24'): 1,
                                  ('25', '25'): 1,
                                  ('26', '26'): 1,
                                  ('27', '27'): 10,
                                  ('28', '28'): 1,
                                  ('6', '7'): 1,
                                  ('8', '9'): 1,
                                  ('9', '10'): 1,
                                  ('10', '11'): 1,
                                  ('11', '12'): 1,
                                  ('12', '13'): 1,
                                  ('13', '14'): 1,
                                  ('14', '15'): 1,
                                  ('15', '16'): 1,
                                  ('16', '17'): 1,
                                  ('18', '19'): 1,
                                  ('19', '20'): 1,
                                  ('20', '21'): 1,
                                  ('23', '24'): 1,
                                  ('24', '25'): 1,
                                  ('25', '26'): 1,
                                  ('26', '27'): 1,
                                  ('27', '28'): 1,
                                  ('28', '29'): 1,
                                  ('4', '5'): 1,
                                  ('5', '5'): 1,
                                  ('5', '6'): 1,
                                  ('6', '6'): 1},
                  'arrival_times': {'12': 27,
                                    '15': 42,
                                    '19': 49,
                                    '24': 58,
                                    '27': 64,
                                    '29': 77, '5': 80,
                                    '9': 88},
                  'departure_times': {'12': 37,
                                      '15': 43,
                                      '19': 50,
                                      '24': 59,
                                      '27': 74,
                                      '5': 81,
                                      '9': 89}},
        'RE_0': {'start': 11,
                 'traveltimes': {('0', '1'): 1,
                                 ('1', '2'): 1,
                                 ('2', '3'): 2,
                                 ('3', '4'): 2,
                                 ('4', '4'): 2,
                                 ('5', '5'): 2,
                                 ('6', '6'): 1,
                                 ('7', '8'): 1,
                                 ('8', '8'): 2,
                                 ('9', '9'): 2,
                                 ('10', '10'): 1,
                                 ('11', '11'): 1,
                                 ('14', '14'): 1,
                                 ('15', '15'): 2,
                                 ('16', '16'): 2,
                                 ('17', '18'): 2,
                                 ('18', '18'): 1,
                                 ('21', '22'): 1,
                                 ('22', '23'): 1,
                                 ('23', '23'): 1,
                                 ('24', '24'): 2,
                                 ('25', '25'): 2,
                                 ('26', '26'): 1,
                                 ('4', '5'): 2,
                                 ('5', '6'): 2,
                                 ('6', '7'): 2,
                                 ('8', '9'): 1,
                                 ('9', '10'): 2,
                                 ('10', '11'): 1,
                                 ('13', '14'): 2,
                                 ('14', '15'): 1,
                                 ('15', '16'): 1,
                                 ('16', '17'): 1,
                                 ('20', '21'): 1,
                                 ('23', '24'): 1,
                                 ('24', '25'): 1,
                                 ('25', '26'): 2,
                                 ('28', '29'): 1,
                                 ('11', '12'): 2,
                                 ('12', '12'): 4,
                                 ('12', '13'): 2,
                                 ('13', '13'): 1,
                                 ('18', '19'): 2,
                                 ('19', '19'): 2,
                                 ('19', '20'): 1,
                                 ('20', '20'): 1,
                                 ('26', '27'): 1,
                                 ('27', '27'): 4,
                                 ('27', '28'): 1,
                                 ('28', '28'): 1},
                 'arrival_times': {'12': 18, '15': 29,
                                   '19': 40, '24': 51,
                                   '27': 60, '29': 67,
                                   '5': 73, '9': 86},
                 'departure_times': {'12': 22,
                                     '15': 31,
                                     '19': 42,
                                     '24': 53,
                                     '27': 64,
                                     '5': 75,
                                     '9': 88}},
        'RE_1': {'start': 31,
                 'traveltimes': {('0', '1'): 1,
                                 ('1', '2'): 1,
                                 ('2', '3'): 2,
                                 ('3', '4'): 2,
                                 ('4', '4'): 2,
                                 ('7', '8'): 1,
                                 ('8', '8'): 2,
                                 ('9', '9'): 2,
                                 ('10', '10'): 1,
                                 ('11', '11'): 1,
                                 ('14', '14'): 1,
                                 ('15', '15'): 2,
                                 ('16', '16'): 2,
                                 ('17', '18'): 2,
                                 ('18', '18'): 1,
                                 ('19', '19'): 2,
                                 ('20', '20'): 1,
                                 ('21', '22'): 1,
                                 ('22', '23'): 1,
                                 ('23', '23'): 1,
                                 ('24', '24'): 2,
                                 ('25', '25'): 2,
                                 ('26', '26'): 1,
                                 ('6', '7'): 2,
                                 ('8', '9'): 1,
                                 ('9', '10'): 2,
                                 ('10', '11'): 1,
                                 ('13', '14'): 2,
                                 ('14', '15'): 1,
                                 ('15', '16'): 1,
                                 ('16', '17'): 1,
                                 ('18', '19'): 2,
                                 ('19', '20'): 1,
                                 ('20', '21'): 1,
                                 ('23', '24'): 1,
                                 ('24', '25'): 1,
                                 ('25', '26'): 2,
                                 ('28', '29'): 1,
                                 ('11', '12'): 2,
                                 ('12', '12'): 4,
                                 ('12', '13'): 2,
                                 ('13', '13'): 1,
                                 ('26', '27'): 1,
                                 ('27', '27'): 4,
                                 ('27', '28'): 1,
                                 ('28', '28'): 1,
                                 ('4', '5'): 2,
                                 ('5', '5'): 2,
                                 ('5', '6'): 2,
                                 ('6', '6'): 1},
                 'arrival_times': {'12': 38, '15': 49,
                                   '19': 60, '24': 71,
                                   '27': 80, '29': 87,
                                   '5': 93, '9': 106},
                 'departure_times': {'12': 42,
                                     '15': 51,
                                     '19': 62,
                                     '24': 73,
                                     '27': 84,
                                     '5': 95,
                                     '9': 108}},
        'RE_2': {'start': 51,
                 'traveltimes': {('0', '1'): 1,
                                 ('1', '2'): 1,
                                 ('2', '3'): 2,
                                 ('3', '4'): 2,
                                 ('4', '4'): 2,
                                 ('7', '8'): 1,
                                 ('8', '8'): 2,
                                 ('9', '9'): 2,
                                 ('10', '10'): 1,
                                 ('11', '11'): 1,
                                 ('14', '14'): 1,
                                 ('15', '15'): 2,
                                 ('16', '16'): 2,
                                 ('17', '18'): 2,
                                 ('18', '18'): 1,
                                 ('19', '19'): 2,
                                 ('20', '20'): 1,
                                 ('21', '22'): 1,
                                 ('22', '23'): 1,
                                 ('23', '23'): 1,
                                 ('24', '24'): 2,
                                 ('25', '25'): 2,
                                 ('26', '26'): 1,
                                 ('6', '7'): 2,
                                 ('8', '9'): 1,
                                 ('9', '10'): 2,
                                 ('10', '11'): 1,
                                 ('13', '14'): 2,
                                 ('14', '15'): 1,
                                 ('15', '16'): 1,
                                 ('16', '17'): 1,
                                 ('18', '19'): 2,
                                 ('19', '20'): 1,
                                 ('20', '21'): 1,
                                 ('23', '24'): 1,
                                 ('24', '25'): 1,
                                 ('25', '26'): 2,
                                 ('28', '29'): 1,
                                 ('11', '12'): 2,
                                 ('12', '12'): 4,
                                 ('12', '13'): 2,
                                 ('13', '13'): 1,
                                 ('26', '27'): 1,
                                 ('27', '27'): 4,
                                 ('27', '28'): 1,
                                 ('28', '28'): 1,
                                 ('4', '5'): 2,
                                 ('5', '5'): 2,
                                 ('5', '6'): 2,
                                 ('6', '6'): 1},
                 'arrival_times': {'12': 58, '15': 69,
                                   '19': 80, '24': 91,
                                   '27': 100,
                                   '29': 107,
                                   '5': 113,
                                   '9': 126},
                 'departure_times': {'12': 62,
                                     '15': 71,
                                     '19': 82,
                                     '24': 93,
                                     '27': 104,
                                     '5': 115,
                                     '9': 128}},
        'RE_3': {'start': 71,
                 'traveltimes': {('0', '1'): 1,
                                 ('1', '2'): 1,
                                 ('2', '3'): 2,
                                 ('3', '4'): 2,
                                 ('4', '4'): 2,
                                 ('7', '8'): 1,
                                 ('8', '8'): 2,
                                 ('9', '9'): 2,
                                 ('10', '10'): 1,
                                 ('11', '11'): 1,
                                 ('14', '14'): 1,
                                 ('15', '15'): 2,
                                 ('16', '16'): 2,
                                 ('17', '18'): 2,
                                 ('18', '18'): 1,
                                 ('21', '22'): 1,
                                 ('22', '23'): 1,
                                 ('23', '23'): 1,
                                 ('24', '24'): 2,
                                 ('25', '25'): 2,
                                 ('26', '26'): 1,
                                 ('6', '7'): 2,
                                 ('8', '9'): 1,
                                 ('9', '10'): 2,
                                 ('10', '11'): 1,
                                 ('13', '14'): 2,
                                 ('14', '15'): 1,
                                 ('15', '16'): 1,
                                 ('16', '17'): 1,
                                 ('20', '21'): 1,
                                 ('23', '24'): 1,
                                 ('24', '25'): 1,
                                 ('25', '26'): 2,
                                 ('28', '29'): 1,
                                 ('11', '12'): 2,
                                 ('12', '12'): 4,
                                 ('12', '13'): 2,
                                 ('13', '13'): 1,
                                 ('18', '19'): 2,
                                 ('19', '19'): 2,
                                 ('19', '20'): 1,
                                 ('20', '20'): 1,
                                 ('26', '27'): 1,
                                 ('27', '27'): 4,
                                 ('27', '28'): 1,
                                 ('28', '28'): 1,
                                 ('4', '5'): 2,
                                 ('5', '5'): 2,
                                 ('5', '6'): 2,
                                 ('6', '6'): 1},
                 'arrival_times': {'12': 78, '15': 89,
                                   '19': 100,
                                   '24': 111,
                                   '27': 120,
                                   '29': 127,
                                   '5': 133,
                                   '9': 146},
                 'departure_times': {'12': 82,
                                     '15': 91,
                                     '19': 102,
                                     '24': 113,
                                     '27': 124,
                                     '5': 135,
                                     '9': 148}},
        'RE_4': {'start': 91,
                 'traveltimes': {('0', '1'): 1,
                                 ('1', '2'): 1,
                                 ('2', '3'): 2,
                                 ('3', '4'): 2,
                                 ('4', '4'): 2,
                                 ('5', '5'): 2,
                                 ('6', '6'): 1,
                                 ('7', '8'): 1,
                                 ('8', '8'): 2,
                                 ('9', '9'): 2,
                                 ('10', '10'): 1,
                                 ('11', '11'): 1,
                                 ('14', '14'): 1,
                                 ('15', '15'): 2,
                                 ('16', '16'): 2,
                                 ('17', '18'): 2,
                                 ('18', '18'): 1,
                                 ('19', '19'): 2,
                                 ('20', '20'): 1,
                                 ('21', '22'): 1,
                                 ('22', '23'): 1,
                                 ('23', '23'): 1,
                                 ('24', '24'): 2,
                                 ('25', '25'): 2,
                                 ('26', '26'): 1,
                                 ('4', '5'): 2,
                                 ('5', '6'): 2,
                                 ('6', '7'): 2,
                                 ('8', '9'): 1,
                                 ('9', '10'): 2,
                                 ('10', '11'): 1,
                                 ('13', '14'): 2,
                                 ('14', '15'): 1,
                                 ('15', '16'): 1,
                                 ('16', '17'): 1,
                                 ('18', '19'): 2,
                                 ('19', '20'): 1,
                                 ('20', '21'): 1,
                                 ('23', '24'): 1,
                                 ('24', '25'): 1,
                                 ('25', '26'): 2,
                                 ('28', '29'): 1,
                                 ('11', '12'): 2,
                                 ('12', '12'): 4,
                                 ('12', '13'): 2,
                                 ('13', '13'): 1,
                                 ('26', '27'): 1,
                                 ('27', '27'): 4,
                                 ('27', '28'): 1,
                                 ('28', '28'): 1},
                 'arrival_times': {'12': 98,
                                   '15': 109,
                                   '19': 120,
                                   '24': 131,
                                   '27': 140,
                                   '29': 147,
                                   '5': 153,
                                   '9': 166},
                 'departure_times': {'12': 102,
                                     '15': 111,
                                     '19': 122,
                                     '24': 133,
                                     '27': 144,
                                     '5': 155,
                                     '9': 168}}},
    'new_trains_traveltimes': {'new_train': {'start': 5,
                                             'traveltimes': {('0', '1'): 1, ('1', '2'): 1, ('2', '3'): 2, ('3', '4'): 2,
                                                             ('4', '4'): 2, ('4', '5'): 2, ('5', '5'): 2, ('5', '6'): 2,
                                                             ('6', '6'): 1, ('6', '7'): 2, ('7', '8'): 1, ('8', '8'): 2,
                                                             ('8', '9'): 1, ('9', '9'): 2, ('9', '10'): 2,
                                                             ('10', '10'): 1, ('10', '11'): 1, ('11', '11'): 1,
                                                             ('11', '12'): 2, ('12', '12'): 4, ('12', '13'): 2,
                                                             ('13', '13'): 1, ('13', '14'): 2, ('14', '14'): 1,
                                                             ('14', '15'): 1, ('15', '15'): 2, ('15', '16'): 1,
                                                             ('16', '16'): 2, ('16', '17'): 1, ('17', '18'): 2,
                                                             ('18', '18'): 1, ('18', '19'): 2, ('19', '19'): 2,
                                                             ('19', '20'): 1, ('20', '20'): 1, ('20', '21'): 1,
                                                             ('21', '22'): 1, ('22', '23'): 1, ('23', '23'): 1,
                                                             ('23', '24'): 1, ('24', '24'): 2, ('24', '25'): 1,
                                                             ('25', '25'): 2, ('25', '26'): 2, ('26', '26'): 1,
                                                             ('26', '27'): 1, ('27', '27'): 4, ('27', '28'): 1,
                                                             ('28', '28'): 1, ('28', '29'): 1},
                                             'arrival_times': {'12': 12, '15': 23, '19': 34, '24': 45, '27': 54,
                                                               '29': 61, '5': 67, '9': 80},
                                             'departure_times': {'12': 16, '15': 25, '19': 36, '24': 47, '27': 58,
                                                                 '5': 69, '9': 82}}}, 'timehorizon': 201}
