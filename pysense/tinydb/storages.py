import json
from os.path import exists
from simplecrypt import encrypt, decrypt
from tinydb.storages import Storage

class CryptStorage(Storage):
    def __init__(self, filename, password):
        self.filename = filename
        self.password = password

    def read(self):
        if exists(self.filename):
            with open(self.filename, 'rb') as handle:
                cipherdb = handle.read()
                jsondb = decrypt(self.password, cipherdb)
                data = json.loads(jsondb.decode('utf8'))
                return data
        else:
            return {}

    def write(self, data):
        with open(self.filename, 'wb') as handle:
            cipherdb = encrypt(self.password, json.dumps(data))
            handle.write(cipherdb)

    def close(self):
        unlink(self.filename)

