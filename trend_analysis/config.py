"""Load configuration from a file and return an object"""


import os
import re
import yaml
from . import constants as const


def config_postprocess(cfg):
    """Run processing on config loaded from file"""
    env_pattern = re.compile(r'\(.*\)$ENV(\'\(\w+\)\')\(.*\)$')
    mutated_cfg = cfg
    return mutated_cfg


def get_config():
    """Get configuration from a file"""
    if not os.path.isfile(const.CFG_FILE):
        raise RuntimeError(f'Config file not found: {const.CFG_FILE}')
    with open(const.CFG_FILE) as cfg_f:
        cfg = yaml.load(cfg_f)
    return config_postprocess(cfg)
