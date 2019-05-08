from threading import Timer
from abc import abstractmethod

from pysense.logger import pysense_logger

thoughts = {}


class ThoughtBase():

    def schedule(self, **kwargs):
        self.schedule_options = kwargs
        self.scheduled_run()

    def scheduled_run(self):
        self.run()
        self.job = Timer(self.schedule_options['after'], self.scheduled_run)
        self.job.start()

    def stop(self):
        pysense_logger.info(' stopping... ')
        if hasattr(self, 'job'):
            pysense_logger.info('stop job')
            self.job.cancel()

    @abstractmethod
    def run(self):
        pass
