from os.path import join, expanduser
from os import environ


HOME = expanduser('~/.sense')
TINY_DB_PATH = join(HOME, "db.cipher")
THOUGHTS_PATH = join(HOME, "thoughts")
ICONS_PATH = join(HOME, "icons")
URI_FILE = join(HOME, "uri")
SOURCES_FILE = join(HOME, "sources.py")
GUI = environ.get("DISPLAY") is not None
LOG_FILE = join(HOME, "sense.log")
