import json
from os.path import exists
from simplecrypt import encrypt, decrypt
from tinydb.storages import Storage

class CryptStorage(Storage):
    def __init__(self, filename, password):
        self.filename = filename
        self.password = password
        self.in_memory = None

    def read(self):
        if self.in_memory:
            return self.in_memory
        if exists(self.filename):
            with open(self.filename, 'rb') as handle:
                cipherdb = handle.read()
                jsondb = decrypt(self.password, cipherdb)
                data = json.loads(jsondb.decode('utf8'))
                self.in_memory = data
                return data
        else:
            return {}

    def write(self, data):
        self.in_memory = data
        with open(self.filename, 'wb') as handle:
            cipherdb = encrypt(self.password, json.dumps(data))
            handle.write(cipherdb)

    def close(self):
        unlink(self.filename)

