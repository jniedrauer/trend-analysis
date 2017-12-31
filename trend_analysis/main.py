"""Module entrypoint"""


from . import config


def main():
    """Read config file and run actions"""
    cfg = config.get_config()
