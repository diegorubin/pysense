from tinydb import TinyDB, Query

from pysense.settings import TINY_DB_PATH

def db():
    return TinyDB(TINY_DB_PATH)

def all(table):
    return table.all()

def find_in_table(table, name):
    query = Query()
    return table.search(query.name == name)

def save_in_table(table, name, value):
    attributes = {'name': name, 'value': value}
    query = Query()
    memory = table.search(query.name == name)
    if len(memory) == 0:
        table.insert(attributes)
    else:
        table.update(attributes, query.name == name)

def memories():
    return db().table('memories')

def remember(name, value):
    save_in_table(memories(), name, value)

def remind(name):
    query = Query()
    memory = memories().search(query.name == name)
    if len(memory):
        return memory[0]['value']
    else:
        return None

