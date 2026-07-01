"""
    singleton pattern
            - ensure a class only has one instance, and provide a global point of access to it
"""
class A:
    _instance = None
    def __init__(self):
        _instance = None #_variable => private variable
        raise RuntimeError("call get_instance() instead")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

#------------------------------------------------------------------------------

class Singleton(type):
    _instance = None
    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance

class B(Singleton):
    pass
