from lib.car import Car

class Bmw(Car):
    def __init__(self,modal_name, color):
        Car.__init__(self)
        self.model = modal_name
        self.color = color

    def to_string(self):
        return f"Модель: {self.model}Колёс: {self.wheels}\nЦвет: {self.color}"