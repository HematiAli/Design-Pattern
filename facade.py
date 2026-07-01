"""
    Facade structural design pattern that provides a simplified interface to library , framework or any other complex
    set of classes.
"""
class CPU: # subsystem
    
    def execute(self):
        print("executing...")

class Memory: # subsystem
    def load(self):
        print("loading data...")

class SSD: # subsystem
    def read(self):
        print("reading from ssd...")

class Computer: #Facad
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SSD()
    def start(self):
        self.cpu.execute()
        self.memory.load()
        self.ssd.read()

def clinet():
    computer = Computer()
    computer.start()
clinet()