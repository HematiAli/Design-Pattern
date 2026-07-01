"""
    Factory         is a creational design pattern that provides an interface for creation objects
        in a superclass, but allows subclasses to alter the type of objects that will be created
"""
from abc import ABC, abstractmethod

class File(ABC): # creator
    def __init__(self, file):
        self.file = file

    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        product = self.make()
        result = product.edit(self.file)
        return result

class JsonFile(File): # creator
    def make(self):
        return Json()

class XmlFile(File): # creator
    def make(self):
        return Xml()



class Json: # product
    def edit(self, file):
        return f"Working on {file} json"

class Xml: # product
    def edit(self, file):
        return f"Working on {file} xml"


def client(file, format):
    formats = {
        'json': JsonFile,
        'xml': XmlFile
    }
    result = formats[format](file)
    return result.call_edit()

print(client('show', 'xml'))