from vehicles.cpoint_class import CPoint
from vehicles.interfaces_class import ISwimAble
from vehicles.vehicle_class import CVehicle


class CShip(CVehicle, ISwimAble):

    def swim(self):
        return self.speed

    def __init__(self, price, speed, year, port, passangers):
        CVehicle.__init__(self, price, speed, year)
        self.port = port
        self.passangers = passangers

    def set_engine(self):
        pass

    def show(self):
        print("CShip", self.__str__())

    def __str__(self):
        return f"Ship. {CVehicle.__str__(self)}, Origin port: {self.port}, Passengers: {self.passangers}"