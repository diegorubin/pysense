import Pyro4


from sense.memories import remember, remind
from sense.settings import THOUGHTS_PATH
from sense.utils import save_uri
from sense.thought import thoughts
from sense.thought.utils import load_thoughts

@Pyro4.expose
class Daemon(object):
    def remember(self, name, value):
        remember(name, value)
        return 'ok'

    def remind(self, name):
        return remind(name)

    def thoughts(self):
        names = []
        for thought in thoughts:
            names.append(thought)
        return names

    def call(self, command, argv):
        getattr(thoughts[command], argv[2])(argv)


def start():

    load_thoughts(THOUGHTS_PATH)

    daemon = Pyro4.Daemon()
    uri = daemon.register(Daemon)
    save_uri(uri)

    daemon.requestLoop()


