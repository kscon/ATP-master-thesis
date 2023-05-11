# this is a simple implementation of the TEN described in my master thesis
import time
from TEN_additional_train_path_problem import ten_core, draw_ten_utils, ten_input_parser


class TENModel:
    def __init__(self, parsed_data: dict, iteration: int, filepath: str, drawing_timehorizon: (int, int) = (0, 30),
                 draw_tens: int = 0, print_solution: int = 0):
        self.input_data = parsed_data
        self.filepath = filepath
        self.iteration = iteration
        self.drawing_timehorizon = drawing_timehorizon
        self.draw_tens = draw_tens
        self.print_solution = print_solution
        self.ten_core = None
        self.time_dict = {'ten_creation_time': 0.0, 'ten_edge_deletion_time': 0.0, 'ten_pathfinding_time': 0.0,
                          'ten_execution_time': 0.0}

    def execute_ten_model(self):
        # time_dict = {}
        starttime = time.time()

        drawing_starttime, drawing_endtime = self.drawing_timehorizon

        self.ten_core = ten_core.TEN(self.input_data, self.print_solution)
        self.ten_core.add_existing_timetable_to_ten()

        if self.draw_tens == 1:
            draw_ten_utils.draw_ten(self.ten_core.ten,
                                    data={'filepath': self.filepath, 'iteration_counter': self.iteration}, draw_aux=1,
                                    start_time=drawing_starttime, end_time=drawing_endtime)
        ten_creation_time = time.time()

        self.ten_core.edge_preprocessing()

        ten_edge_deletion_time = time.time()

        self.ten_core.pathfinding()

        # draw ten graph
        # p = self.ten_core.pathfinding()
        if self.print_solution == 1:
            print(self.ten_core.resulting_path)
        if self.draw_tens == 1:
            draw_ten_utils.draw_ten(self.ten_core.ten,
                                    data={'filepath': self.filepath, 'iteration_counter': self.iteration},
                                    start_time=drawing_starttime, end_time=drawing_endtime,
                                    new_train_path=self.ten_core.resulting_path)

        ten_pathfinding_time = time.time()
        ten_execution_time = time.time() - starttime
        self.ten_core.generate_timetable_from_path()

        self.time_dict['ten_creation_time'] = ten_creation_time - starttime
        self.time_dict['ten_edge_deletion_time'] = ten_edge_deletion_time - ten_creation_time
        self.time_dict['ten_pathfinding_time'] = ten_pathfinding_time - ten_edge_deletion_time
        self.time_dict['ten_execution_time'] = ten_execution_time

        self.time_dict = {k: round(v, 2) for k, v in self.time_dict.items()}
        print('ten execution time: ' + str(self.time_dict['ten_execution_time']) + 's')
