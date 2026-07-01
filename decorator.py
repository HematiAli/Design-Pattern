"""
    Decorator
        - a structural pattern that allows adding new behaviors to objects dynamically.
        by placing them inside special wrapper object , called decorator
"""
from abc import ABC, abstractmethod

class Page(ABC):

    @abstractmethod
    def show(self):
        pass

class AuthPage(Page):
    def show(self):
        print('Welcome to authenticated page')
class AnonPage(Page):
    def show(self):
        print('Welcome to anonymous page')

class PageDecorator(Page, ABC):
    def __init__(self, component):
        self._component = component
    @abstractmethod
    def show(self):
        pass

class PageAuthDecorator(PageDecorator):
    def show(self):
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        if username == 'root' and password == 'root':
            self._component.show()
        else:
            print('you are not authenticated')

def client():
    page = AuthPage()
    authenticated = PageAuthDecorator(page)
    authenticated.show()
client()