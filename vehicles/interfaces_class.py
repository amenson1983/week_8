import abc
from abc import ABC



class IMoveAble(ABC):
    @abc.abstractmethod
    def move(self): pass


class ISwimAble(ABC):
    @abc.abstractmethod
    def swim(self): pass


class IFlyAble(ABC):
    @abc.abstractmethod
    def fly(self): pass