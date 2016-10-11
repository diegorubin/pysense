import Pyro4
from pysense.utils import recover_uri

class Client():
    def __init__(self):
        uri = recover_uri()
        self.proxy = Pyro4.Proxy(uri)

    def remember(self, name, value):
        return self.proxy.remember(name, value)

    def remind(self, name):
        return self.proxy.remind(name)

    def thoughts(self):
        return self.proxy.thoughts()

    def rethink(self):
        return self.proxy.rethink()

    def learn(self):
        return self.proxy.learn()

    def call(self, command, argv):
        return self.proxy.call(command, argv)

