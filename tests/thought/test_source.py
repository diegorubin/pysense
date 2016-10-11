import unittest
import shutil

from unittest.mock import patch
from os import mkdir
from os.path import join, dirname, isdir, exists

FIXTURES = join(dirname(__file__), 'fixtures')
SOURCES_FILE = join(FIXTURES, 'sources.py')
THOUGHTS_PATH = join(FIXTURES, 'thoughts')

from pysense.thought import source

@patch('pysense.thought.source.SOURCES_FILE', SOURCES_FILE)
@patch('pysense.thought.source.THOUGHTS_PATH', THOUGHTS_PATH)
class TestSource(unittest.TestCase):

    def setUp(self):
        self.__clear_directories__(THOUGHTS_PATH)
        mkdir(THOUGHTS_PATH)

    def tearDown(self):
        self.__clear_directories__(THOUGHTS_PATH)

    def test_update_sources(self):
        source.get_thoughts_from_sources()
        self.assertTrue(exists(join(THOUGHTS_PATH, 'example', 'tasks_thought.py')))

    def __clear_directories__(self, dirname):
        if isdir(dirname):
            shutil.rmtree(dirname)

