# coding=utf-8

"""
logging Class
"""
import logging

logger = logging.getLogger('{}'.format('sys_specific'))
logger.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# create file handler which logs even debug messages
fh = logging.FileHandler('logfile.log'.format())
fh.setLevel(logging.ERROR)
fh.setFormatter(formatter)
logger.addHandler(fh)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)



