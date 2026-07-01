"""
    chain of responsibility
    - a behavioral design pattern
"""
from abc import ABC, abstractmethod
class AbstractHandler(ABC):
    @abstractmethod
    def set_next(self, handler): pass
    @abstractmethod
    def handle(self, request): pass

class BaseHandler(AbstractHandler):
    _next_handler = None
    def set_next(self, handler):
        self._next_handler = handler
        return handler
    def handle(self, request):
        if self._next_handler is not None:
            return self._next_handler.handle(request)
        else:
            return None

class HandlerOne(BaseHandler):
    def handle(self, request):
        if 0 <= request <= 10:
            print(f"HandlerOne is proccessing request {request}")
        else:
            return super().handle(request)
class HandlerTwo(BaseHandler):
    def handle(self, request):
        if 10 < request <= 20:
            print(f"HandlerTwo is proccessing request {request}")
        else:
            return super().handle(request)

class DefaultHandler(BaseHandler):
    def handle(self, request):
        print(f"DefaultHandler is proccessing request {request}")

def client(handler, request):
    for num in request:
        handler.handle(num)

nums = [21, 20, 3, 10]
h1 = HandlerOne()
h2 = HandlerTwo()
h0 = DefaultHandler()

h1.set_next(h2).set_next(h0)

client(h1, nums)