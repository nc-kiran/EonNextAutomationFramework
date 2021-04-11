import os
import logging
from logging.config import dictConfig
from time import strftime

# Log folder directory
LOG_DIR = "logs"
LOGGING_CONFIG = "Debug"

# Logger configuration settings
LOG_SETTINGS = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'formatted_console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'stream': 'ext://sys.stdout',
        },
        'formatted_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': "logs" + os.path.sep + "EonNext_" + strftime("%Y-%m-%d_%H_%M_%S") + ".log",
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
    },
    'formatters': {
        'detailed': {
            'format': '[%(levelname)s] : %(asctime)s : %(filename)s : %(funcName)s:%(lineno)d : %(message)s',
        },
        'blank': {
            'format': '',
        },
    },
    'loggers': {
        'formatted_log': {
                'level': 'DEBUG',
                'handlers': ['formatted_file', 'formatted_console']
            },
    }
}


def setup_logging():
    """Use the LOG_SETTINGS defined above and initialize the logger
    :return: None
    """
    logging.config.dictConfig(LOG_SETTINGS)


def setup_formatted_logging(context):
    """Formatted log includes file name, time stamp and log levels
    :param context: Holds contextual information
    :return: None
    """
    context.logger = logging.getLogger('formatted_log')

