"""
Observer
	- behavioral design pattern
"""
from abc import ABC, abstractmethod
from random import randrange

class Publisher(ABC):
    @abstractmethod
    def subscribe(self, observe): pass
    @abstractmethod
    def unsubscribe(self, observe): pass
    @abstractmethod
    def notify(self): pass

class ConcretePublisher(Publisher):
    _observer = []
    _state = None
    def subscribe(self, observe):
        self._observer.append(observe)
    def unsubscribe(self, observe):
        self._observer.remove(observe)
    def notify(self):
        print("Notifying observes")

        for observe in self._observer:
            observe.update(self)
    def operation(self):
        self._state = randrange(0, 10)
        print(f"state change to {self._state}")
        self.notify()

class Observe(ABC):
    @abstractmethod
    def update(self, publisher): pass

class ObserveA(Observe):
    def update(self, publisher):
        if publisher._state <= 5:
            print("observe A reacted to event.")
class ObserveB(Observe):
    def update(self, publisher):
        if publisher._state > 5:
            print("observe B reacted to event.")

p = ConcretePublisher()
o1 = ObserveA()
o2 = ObserveB()
p.subscribe(o1)
p.subscribe(o2)
p.operation()