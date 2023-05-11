import numpy as np
from network_generator import NetworkGenerator


class NetworkGeneratorMain:
    def __init__(self):
        self.network_generator = None


if __name__ == '__main__':
    number_of_blocks = 8
    small_stations = 1
    big_stations = 1
    slow_trains = 2
    fast_trains = 1
    new_trains_number = 3
    new_trains = []
    list_of_trains = ['s', 'f']
    for i in range(new_trains_number):
        new_trains.append(list_of_trains[np.random.default_rng().integers(0, 2)])
    # new_trains = ['s', 'f', 'f', 'f', 's']

    file_location = 'multiple_new_trains/'  # leave empty to save in networks folder

    for i in range(1):
        ngm = NetworkGeneratorMain()
        ngm.network_generator = NetworkGenerator(
            number_of_blocks=number_of_blocks, small_stations=small_stations, big_stations=big_stations,
            slow_trains=slow_trains, fast_trains=fast_trains, new_trains=new_trains, file_location=file_location)
        ngm.network_generator.run_network_generator(check_timetable_feasibility=1, overwrite_generated_timetable=1)
