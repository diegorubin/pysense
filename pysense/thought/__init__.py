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
        self.job = Timer(self.schedule_options['after'], self.scheduled_run)
        self.job.start()

    def stop(self):
        print(' stopping... ')
        if hasattr(self, 'job'):
            print('stop job')
            self.job.cancel()

    @abstractmethod
    def run(self):
        pass

