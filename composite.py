"""
    Composite a structural design pattern
"""
from abc import ABC, abstractmethod
class Being(ABC):
    def add(self): pass
    def remove(self): pass
    def is_composite(self): return False
    @abstractmethod
    def execute(self): pass

class Animal(Being):
    def __init__(self, name):
        self.name = name
    def execute(self):
        print(f"Animal {self.name}")

class Human(Being):
    def __init__(self):
        self._children = []

    def add(self, child):
        self._children.append(child)
    def remove(self, child):
        self._children.remove(child)
    def is_composite(self):
        return True
    def execute(self):
        print("Human Composite")
        for child in self._children:
            child.execute()
class Male(Human):
    def __init__(self, name):
        self.name = name
    def is_composite(self):
        return False
    def execute(self):
        print(f"Male {self.name}")

class Female(Human):
    def __init__(self, name):
        self.name = name
    def is_composite(self):
        return False
    def execute(self):
        print(f"Female {self.name}")

def client():
    f1 = Female("eli")
    f2 = Male("katty")
    m1 = Male("ali")
    h1 = Human()
    h1.add(f1)
    h1.add(f2)
    h1.add(m1)
    h1.execute()
client()