"""
    Proxy
"""
from abc import ABC, abstractmethod
import time
from datetime import datetime

class AbstractServer(ABC):
    @abstractmethod
    def recieve(self):
        pass

class Server(AbstractServer):
    def recieve(self):
        print("processing your request")
        time.sleep(1)
        print("Done....")

class LogProxy(AbstractServer):
    def __init__(self, server):
        self._server = server
    def recieve(self):
        self.logging()
        self._server.recieve()

    def logging(self):
        with open('log.log', 'a') as log:
            log.write(f"Request {datetime.now()}\n")

def client(server, proxy):
    s = server()
    p = proxy(s)
    p.recieve()

client(Server, LogProxy)