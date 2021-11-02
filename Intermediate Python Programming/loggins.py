import logging
import traceback
from logging.handlers import RotatingFileHandler
'''
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -%(levelname)s  - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
logging.debug('This is a debug message')
logging.info('this is an information message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
'''
logger = logging.getLogger(__name__)
#create handle
steam_h = logging.StreamHandler()
file_h = logging.FileHandler('File.log')

#level and the format
steam_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s  -%(name)s -%(levelname)s  - %(message)s')
steam_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(steam_h)
logger.addHandler(file_h)

logger.warning('This is a warning')
logger.error('This is a error')

try:
    a = [1,2,3]
    val = a[4]
except:
    logging.error('The error is %s', traceback.format_exc())

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#roll over after 5kb
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info("hello world")