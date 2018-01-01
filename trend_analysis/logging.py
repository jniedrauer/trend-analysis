"""Module wide logging configuration"""


import logging
from logging.handlers import RotatingFileHandler


def init_logging(cfg):
    """Initialize logging with configuration"""
    # File logger
    logging.getLogger().setLevel(logging.DEBUG) # Set root logger base level
    log_format = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    log_file = RotatingFileHandler(
        cfg['logging']['file'],
        maxBytes=1000000,
        backupCount=3
    )
    log_file.setFormatter(log_format)
    log_file.setLevel(cfg['logging']['level'])
    logging.getLogger().addHandler(log_file)

    # Console logger
    log_console = logging.StreamHandler()
    log_console.setFormatter(logging.Formatter('%(message)s'))
    log_console.setLevel(cfg['logging']['level'])
    logging.getLogger().addHandler(log_console)
