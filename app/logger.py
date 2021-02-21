import logging
from sys import stdout

_ROOT_LOGGER = None

def initialize_root_logger():
    _ROOT_LOGGER = logging.getLogger()
    _ROOT_LOGGER.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler(stdout)
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    _ROOT_LOGGER.addHandler(console_handler)

    _ROOT_LOGGER.debug("Root logger initialized")
