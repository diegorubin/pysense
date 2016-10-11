from os.path import exists
from os import makedirs

from pysense.settings import HOME, THOUGHTS_PATH, URI_FILE

def init_dir():
    if not exists(HOME):
        print('creating home dir')
        makedirs(HOME)

    if not exists(THOUGHTS_PATH):
        print('creating thoughts path')
        makedirs(THOUGHTS_PATH)

def save_uri(uri):
    with open(URI_FILE, "w") as uri_file:
        return uri_file.write(str(uri))

def recover_uri():
    with open(URI_FILE) as uri_file:
        return ''.join(uri_file.readlines())

