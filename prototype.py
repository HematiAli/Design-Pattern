"""
    Prototype
        -Prototype is a creational design pattern that lets you copy existing objects
        without making your code dependent on their classes.
"""
import copy
from os import name


class Prototype:
    def __init__(self):
        self._objects = {}
    def register(self, name, obj):
        self._objects[name] = obj
    def unregister(self, name):
        del self._objects[name]
    def clone(self, name, **kwargs):
        cloned_obj = copy.deepcopy(copy.deepcopy(self._objects[name]))
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj

def client(name, obj, **kwargs):
    prototype = Prototype()
    prototype.register(name, obj)
    return prototype.clone(name, **kwargs)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('ali', 22)

p_clone = client('p1', p, age=20)
p_clone2 = client('p2', p_clone, age=19)

print(p_clone2.__dict__)

