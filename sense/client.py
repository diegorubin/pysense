import Pyro4
from utils import recover_uri

class Client():
    def __init__(self):
        uri = recover_uri()
        self.proxy = Pyro4.Proxy(uri)

    def remember(self, name, value):
        self.proxy.remember(name, value)

