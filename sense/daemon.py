import Pyro4

from tinydb import TinyDB

from sense.settings import TINY_DB_PATH, THOUGHTS_PATH
from sense.utils import save_uri
from sense.thought.utils import load_thoughts

@Pyro4.expose
class Daemon(object):
    def remember(self, name, value):
        print 'remember called'
        return 'ok'

    def db(self):
        if self.db is None:
            self.db = TinyDB(TINY_DB_PATH)
        return self.db


def start():

    load_thoughts(THOUGHTS_PATH)

    daemon = Pyro4.Daemon()
    uri = daemon.register(Daemon)
    save_uri(uri)

    daemon.requestLoop()


