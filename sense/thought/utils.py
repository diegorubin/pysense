import imp
import os

from sense.thought import thoughts

def load_thoughts(path):
    for f in os.listdir(path):
        if(f.endswith("_thought.py")):
            name = f.replace('.py', '')
            module = imp.load_source(name, os.path.join(path, f))
            thoughts[name] = module.init()

