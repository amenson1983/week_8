from vehicles.ccar_class import CCar
from vehicles.interfaces_class import *


class Amfibia(CCar, ISwimAble,IMoveAble):
    def __init__(self, price, speed, year,passangers):
        super().__init__(price, speed, year,passangers)


    def swim(self):
        return self.speed / 2
    def move(self):
        return self.speed
    def __str__(self):
        return f'Amfibia. Year: {super().year}, Price: {super().price},Speed: {super().speed}, Passengers: {self.passangers}'
    def __repr__(self):
        return f'{super().__str__()},{self.passangers}'