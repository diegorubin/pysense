"""
Settings for application logging
"""
import logging

from pysense.settings import LOG_FILE

LOG_FORMAT = '%(asctime)s|%(name)s|%(thought)s|%(levelname)s: %(message)s'


class CustomLogger(logging.Logger):
    """
    Custom logger implementation
    """

    def _log(self, level, msg, args,
             exc_info=None, extra=None, stack_info=None):
        if extra is None:
            extra = {}
        if 'thought' not in extra:
            extra['thought'] = 'core'
        super(CustomLogger, self)._log(
            level, msg, args, exc_info, extra, stack_info)


logging.setLoggerClass(CustomLogger)
pysense_logger = logging.getLogger('pysense')
pysense_logger.propagate = 0
pysense_logger.setLevel(getattr(logging, 'DEBUG'))

PYSENSE_FORMATTER = logging.Formatter(LOG_FORMAT, datefmt='%Y-%m-%d %H:%M:%S')

if LOG_FILE:
    PYSENSE_HANDLER = logging.FileHandler(LOG_FILE)
    PYSENSE_HANDLER.setFormatter(PYSENSE_FORMATTER)
    pysense_logger.addHandler(PYSENSE_HANDLER)

PYSENSE_HANDLER = logging.StreamHandler()
PYSENSE_HANDLER.setFormatter(PYSENSE_FORMATTER)

pysense_logger.addHandler(PYSENSE_HANDLER)
