class CPoint():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if -100<value<100:
            self.__x = value
        else:
            self.__x = 0

    def __str__(self):
        return f"[{self.x}, {self.y}]"