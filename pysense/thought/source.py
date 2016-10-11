import git
import os
import shutil
import imp

from os.path import join

from pysense.settings import SOURCES_FILE, THOUGHTS_PATH

def get_thoughts_from_sources():
    sources = __init_sources()
    for source in sources:
        name = source[0]
        address = source[1]

        __clone_repository(join(THOUGHTS_PATH, name), address)


def __init_sources():
    module = imp.load_source('sources', SOURCES_FILE)
    return module.sources

def __clone_repository(dirname, repository):

    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
    os.mkdir(dirname)

    repo = git.Repo.init(dirname)

    origin = repo.create_remote('origin', repository)
    origin.fetch()
    origin.pull(origin.refs[0].remote_head)


