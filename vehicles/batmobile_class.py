from vehicles.ccar_class import CCar
from vehicles.interfaces_class import ISwimAble, IFlyAble, IMoveAble


class BatMobile(CCar, ISwimAble, IFlyAble,IMoveAble):
    def __init__(self, price, speed, year,passangers, height):
        super().__init__(price, speed, year,passangers)
        self.height = height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if 0<value<5000:
            self.__height = value
        else: self.__height = None


    def swim(self):
        return self.speed / 2

    def fly(self):
        return self.speed * 2
    def move(self):
        return self.speed
    def __str__(self):
        return f'Batmobile. {super().__str__()}, Max. height: {self.height}, Passengers: {self.passangers}'