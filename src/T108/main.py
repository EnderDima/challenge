import os

from lib.car import Car
from lib.bmw import Bmw

current_part = os.getcwd()
data_dir = current_part + '/data/'
data_files = os.listdir(data_dir)

#cars = Car.read_from_files(data_dir, data_files)

#for car in cars:
#    print(car.to_string())