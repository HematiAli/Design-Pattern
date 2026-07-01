"""
    Command
    - a behavioral design pattern
"""
from abc import ABC, abstractmethod
class Command(ABC):
    @abstractmethod
    def execute(self): pass

class SimpleCommand(Command):
    def __init__(self, payload):
        self._payload = payload
    def execute(self):
        print(f"SimpleCommand: I can do simple things like printing ({self._payload})")

class ComplexCommand(Command):
    def __init__(self, receiver, a, b):
        self._receiver = receiver
        self._a = a
        self._b = b
    def execute(self):
        print('ComplexCommand: Complex stuff should be done a receiver object', end='')
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)

class Receiver:
    def do_something(self, a):
        print(f'\nReceiver: working on ({a}.)', end="")

    def do_something_else(self, b):
        print(f'\nReceiver: working on ({b}.)', end="")
class Invoker:
    _start = None
    _finish = None

    def set_start(self, command):
        self._start = command
    def set_finish(self, command):
        self._finish = command
    def operation(self):
        self._start.execute()
        self._finish.execute()

invoker = Invoker()
invoker.set_start(SimpleCommand('Say Hi!'))

receiver = Receiver()
invoker.set_finish(ComplexCommand(receiver, 'Send email', 'Save report'))

invoker.operation()
