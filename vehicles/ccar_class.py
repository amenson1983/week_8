from vehicles.cpoint_class import CPoint
from vehicles.interfaces_class import IMoveAble

from vehicles.vehicle_class import CVehicle


class CCar(CVehicle, IMoveAble):
    def move(self):
        return self.speed

    def __init__(self,price,speed,year,passangers):
        CVehicle.__init__(self,price,speed,year)
        self.passangers = passangers

    @property
    def passengers(self):
        return self.__passangers

    @passengers.setter
    def passengers(self, value):
        if 0 < value < 5:
            self.__passangers = value
        else:
            self.__passangers = None

    def set_engine(self):
        self.engine = self.Engine("diesel")

    def show(self):
        print("Car", self.__str__())

    def __str__(self):
        return f"Car. {CVehicle.__str__(self)}, Passengers: {self.passangers}"