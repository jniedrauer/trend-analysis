"""Tests for the config module"""
# pylint: disable=import-error,wrong-import-position,unused-variable

import os
import tempfile
import types
from importlib import reload
import pytest
os.environ['HOME'] = tempfile.gettempdir()
from trend_analysis import config, constants as const


def setup_environment(content: str):
    """Initialize a config file and return its path"""
    cfg_f = tempfile.NamedTemporaryFile()
    cfg_f.write(content.encode())
    cfg_f.seek(0)

    return cfg_f.name


def cfg_setup(content: str, env: dict = None):
    """Initialize a config file and environment"""
    def _outer(func: types.FunctionType):
        def _inner(*args, **kwargs):
            cfg_f = tempfile.NamedTemporaryFile()
            cfg_f.write(content.encode())
            cfg_f.seek(0)
            os.environ['TA_CONFIG_FILE'] = cfg_f.name
            if env:
                for key, value in env.items():
                    os.environ[key] = value
            reload(const)

            func(*args, **kwargs)
        return _inner
    return _outer



@cfg_setup('foo: bar')
def test_load_config_file():
    """Assert that we can actually load a config file"""
    cfg = config.get_config()
    assert cfg['foo'] == 'bar'


def test_load_failed():
    """Assert that error is raised if config is not loaded"""
    os.environ['TA_CONFIG_FILE'] = '/not/a/real/file'

    reload(const)

    with pytest.raises(RuntimeError):
        cfg = config.get_config()


@cfg_setup("value: prefix_$ENV('env')_suffix", {'env': 'test_value'})
def test_env_var_substitution():
    """Test string substitutions"""
    cfg = config.get_config()
    assert cfg['value'] == 'prefix_test_value_suffix'
