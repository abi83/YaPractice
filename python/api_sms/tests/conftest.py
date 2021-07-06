import os
import sys
from os.path import abspath
from os.path import dirname

root_dir = dirname(dirname(abspath(__file__)))
sys.path.append(root_dir)

os.environ['ACCOUNT_SID'] = ''
os.environ['AUTH_TOKEN'] = ''
os.environ['VK_TOKEN'] = ''
os.environ['NUMBER_FROM'] = ''
os.environ['NUMBER_TO'] = ''

pytest_plugins = [
    'tests.fixtures.fixture_twilio',
    'tests.fixtures.fixture_vk',
]
