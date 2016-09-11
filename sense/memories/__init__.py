from tinydb import TinyDB, Query

from sense.settings import TINY_DB_PATH


def memories():
    db = TinyDB(TINY_DB_PATH)
    return db.table('memories')

def remember(name, value):
    attributes = {'name': name, 'value': value}
    query = Query()
    memory = memories().search(query.name == name)
    if len(memory) == 0:
        memories().insert(attributes)
    else:
        memories().update(attributes, query.name == name)

def remind(name):
    query = Query()
    memory = memories().search(query.name == name)
    if len(memory):
        return memory[0]['value']
    else:
        return None

