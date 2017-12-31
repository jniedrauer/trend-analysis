"""Load configuration from a file and return an object"""


import os
import yaml
from . import constants as const


def get_config():
    """Get configuration from a file"""
    if not os.path.isfile(const.CFG_FILE):
        raise RuntimeError(f'Config file not found: {const.CFG_FILE}')
    with open(const.CFG_FILE) as cfg_f:
        return yaml.load(cfg_f)
