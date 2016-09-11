import time

from threading import Timer
from abc import abstractmethod

thoughts = {}

class ThoughtBase():

    def schedule(self, **kwargs):
        self.schedule_options = kwargs;
        self.scheduled_run()

    def scheduled_run(self):
        self.run()
        Timer(self.schedule_options['after'], self.scheduled_run).start()


    @abstractmethod
    def run(self):
        pass


