import os
from utils.config import config


def get_heartrate():
    heart_filepath = config['global']['heart_filepath']
    MAC = config['global']['bandmac']
    heart = os.popen("python {} {}".format(heart_filepath, MAC))
    print("python {} {}".format(heart_filepath, MAC))
    return heart.read().strip()
