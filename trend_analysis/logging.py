"""Module wide logging configuration"""


import logging


def init_logging(cfg):
    """Initialize logging with configuration"""
    # File logger
    log_path = cfg['logging']['file']

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
    log_console = StreamHandler()
    log_console.setFormatter(logging.Formatter('%(message)s'))
    log_console.setLevel(log_level_to_constant(kwargs.get('loglevel')))
    logging.getLogger().addHandler(log_console)
