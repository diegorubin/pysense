import Pyro4


from pysense.memories import remember, remind
from pysense.settings import THOUGHTS_PATH
from pysense.utils import save_uri
from pysense.thought import thoughts
from pysense.thought import source
from pysense.thought.utils import load_thoughts

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

    def learn(self):
        try:
            source.get_thoughts_from_sources()
            return 'ok'
        except FileNotFoundError as e:
            return 'sources file not found'

    def rethink(self):
        for thought in thoughts:
            print(thought)
            thoughts[thought].stop()

        load_thoughts(THOUGHTS_PATH)
        return 'reloaded'

    def call(self, command, argv):
        return getattr(thoughts[command], argv[2])(argv)

def start():

    load_thoughts(THOUGHTS_PATH)

    daemon = Pyro4.Daemon()
    uri = daemon.register(Daemon)
    save_uri(uri)

    daemon.requestLoop()


