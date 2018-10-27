import os
from ..util import config

password = config['global']['password']


def reset_bluetooth():
    return os.popen('echo {} | sudo -S hciconfig hci0 reset'.format(password)).read().strip()
