"""
	Bridge
	- a structural design pattern that lets you split a large class into two separate
	hierarchies — abstraction and implementation — which can be developed independently of each other.
"""
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, color):
        self.color = color
    def show(self): pass

class Circle(Shape):
    def show(self):
        self.color.paint(self.__class__.__name__)

class Square(Shape):
    def show(self):
        self.color.paint(self.__class__.__name__)

class Triangle(Shape):
    def show(self):
        self.color.paint(self.__class__.__name__)

class Color(ABC):
    def paint(self, name): pass

class Yellow(Color):
    def paint(self, name):
        print(f"this is a yellow {name}")
class Red(Color):
    def paint(self, name):
        print(f"this is a red {name}")
class Blue(Color):
    def paint(self, name):
        print(f"this is a blue {name}")

bl = Blue()
tr = Triangle(bl)
tr.show()