"""
    Adapter
        - a structural design pattern that allows objects with incompatible interfaces to collaborate.
"""
import xmltodict
class Application:
    def send_request(self):
        return 'data.xml'


class Analytic:
    def recive_request(self, json):
        return json


class Adapter:
    def convert_xml_json(self, file):
        with open(file, 'r') as f:
            obj = xmltodict.parse(f.read())
            return obj


def client():
    sender = Application().send_request()
    converted_data = Adapter().convert_xml_json(sender)
    receiver = Analytic().recive_request(converted_data)
    print(receiver)

client()