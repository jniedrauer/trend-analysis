"""Constants for the module"""


import os


CFG_FILE = os.environ.get('TA_CONFIG_FILE') or os.path.join(
    os.environ['HOME'],
    '.trend-analysis.yml'
)
