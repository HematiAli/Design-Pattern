"""
	Abstract Factory
	- Abstract Factory Pattern serves to provide an interface for creating related/dependent
	 objects without need to specify their actual class.

	 Car => Benz, Bmw => Suv, Coupe
			benz suv => gla
			bmw suv => x1
			benz coupe => cls
			bmw coupe => m2
"""
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def call_suv(self):
        pass
    @abstractmethod
    def call_coupe(self):
        pass

class Benz(Car):
    def call_suv(self):
        return Gla()
    def call_coupe(self):
        return Cls()

class Bmw(Car):
    def call_suv(self):
        return X1()
    def call_coupe(self):
        return M2()

class Suv(ABC):
    @abstractmethod
    def create_suv(self):
        pass

class Coupe(ABC):
    @abstractmethod
    def create_coupe(self):
        pass

class Gla(Suv):
    def create_suv(self):
        print("this is your suv benz gla...")

class X1(Suv):
    def create_suv(self):
        print("this is your suv bmw x1...")

class Cls(Coupe):
    def create_coupe(self):
        print("this is your coupe benz cls...")
class M2(Coupe):
    def create_coupe(self):
        print("this is your coupe bmw m2...")

def client_suv(order):
    brands = {
        'benz': Benz,
        'bmw': Bmw
    }
    suv = brands[order]().call_suv()
    suv.create_suv()

def client_coupe(order):
    brands = {
        'benz': Benz,
        'bmw': Bmw
    }
    coupe = brands[order]().call_coupe()
    coupe.create_coupe()

brand = input("benz or bmw: ")
type_car = input("suv or coupe: ")
if type_car == "suv":
    client_suv(brand)
else:
    client_coupe(brand)
