"""Load configuration from a file and return an object"""


import os
import re
import yaml
from . import constants as const


ENV_VAR_PATTERN = re.compile(r"(.*)\$ENV\('(\w+)'\)(.*)$")


def env_var_constructor(loader, node):
    """Substitute match for environment variable"""
    value = loader.construct_scalar(node)
    prefix, env_var, suffix = ENV_VAR_PATTERN.match(value).groups()
    return prefix + os.environ[env_var] + suffix


def get_config():
    """Get configuration from a file"""
    if not os.path.isfile(const.CFG_FILE):
        raise RuntimeError(f'Config file not found: {const.CFG_FILE}')

    # Set up environment variable substitution
    yaml.add_implicit_resolver('!env_var', ENV_VAR_PATTERN)
    yaml.add_constructor('!env_var', env_var_constructor)

    with open(const.CFG_FILE) as cfg_f:
        return yaml.load(cfg_f)
