"""Module entrypoint"""


import logging
from . import config
from .logging import init_logging


def main():
    """Read config file and run actions"""
    cfg = config.get_config()
    init_logging(cfg)
    log = logging.getLogger(__name__)
    log.debug('Hello world')
