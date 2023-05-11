from common_data.timetabling import Timetabling
from MIP_train_timetable_problem import mip_input_parser

file_string = "multiple_new_trains/10b_3s_6et_2nt_123t_365"  # without .py

parsed_data = mip_input_parser.parse_input(filepath=file_string, operating_mode=1)
tt = Timetabling(parsed_data=parsed_data, file_name_string=file_string)
tt.check_timetable_feasibility()
tt.compare_generated_and_feasible_timetable()
# ng.overwrite_current_with_feasible_timetable()

