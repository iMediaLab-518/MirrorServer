import os
from utils.config import config

password = config['global']['password']
heart_filepath = config['global']['heart_filepath']
MAC = config['global']['bandmac']


def get_heartrate():
    heart = os.popen("echo {} | sudo -S python {} {}".format(password, heart_filepath, MAC))
    return heart.read().strip()


def reset_bluetooth():
    return os.popen('echo {} | sudo -S hciconfig hci0 reset'.format(password)).read().strip()


def band_init():
    return os.popen("echo {} | sudo -S python {} {} init".format(password, heart_filepath, MAC)).read().strip()
