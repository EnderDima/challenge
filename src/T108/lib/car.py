class Car:

    @staticmethod
    def read_from_files(dir_name, files):
        cars = []
        for file_name in files:
            file = open(dir_name + file_name, "r", encoding='utf-8')
            lines = file.readlines()
            file.close

            from .bmw import Bmw
            car = Bmw(lines[0], lines[1])
            cars.append(car)
        return cars

    def __init__(self):
        self.wheels = 4

    def to_string(self):
        raise NotImplementedError("Необходимо переопределить метод")

    def ride(self, start_point, destination):
        pass
