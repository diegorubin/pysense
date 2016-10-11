import imp
import os

from pysense.thought import thoughts

def load_thoughts(path):
    for f in os.listdir(path):
        file_path = os.path.join(path, f)
        if (os.path.isdir(file_path)):
            load_thoughts(file_path)
        if (f.endswith("_thought.py")):
            name = f.replace('.py', '')
            module = imp.load_source(name, file_path)
            thoughts[name.replace('_thought', '')] = module.init()

