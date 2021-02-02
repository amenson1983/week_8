import abc


class CVehicle(metaclass=abc.ABCMeta):
    class Engine():
        def __init__(self, fuel):
            self.fuel = fuel

    def __init__(self, price, speed, year):
        self.year = year
        self.speed = speed
        self.price = price
        self.engine = None

    @abc.abstractmethod
    def set_engine(self): pass
    def get_engine(self):
        return self.engine

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if 1900<value<2022:
            self.__year = value
        else: self.__year = None

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0<value<10000:
            self.__speed = value
        else: self.__speed = None

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @abc.abstractmethod
    def show(self): pass

    def __str__(self):
        return f"Year: {self.year}, Price: {self.price}, Speed: {self.speed}"
    def __repr__(self):
        return f"{self.year}, {self.price}, {self.speed}"