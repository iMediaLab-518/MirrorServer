import os
from utils.config import config


def get_weight():
    weight_filepath = config['global']['weight_filepath']
    password = config['global']['password']
    MAC = config['global']['weightmac']
    weight = os.popen("echo {} | sudo -S python {} {}".format(password, weight_filepath, MAC))
    return weight.read().strip()
