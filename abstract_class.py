from abc import ABC,abstractmethod
class Shape(ABC)
    @abstractmethod
    def printarea(self):
        return 0
class Rectangle(shape):
    type="rectange"
    sides=4
    def __init__(self):
        self.length=6
        self.breadth=7
    def priarea(self):
        return self.length*self.breadth
rect1=Rectangle()
rect1.printarea()