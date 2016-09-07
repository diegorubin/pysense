import Pyro4

from tinydb import TinyDB

from sense.settings import TINY_DB_PATH
from sense.utils import save_uri

@Pyro4.expose
class Daemon(object):
    def remember(self, name, value):
        return 'ok'

    def db(self):
        if self.db is None:
            self.db = TinyDB(TINY_DB_PATH)
        return self.db


def start():
    daemon = Pyro4.Daemon()
    uri = daemon.register(Daemon)
    save_uri(uri)

    daemon.requestLoop()


