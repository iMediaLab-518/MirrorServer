from flask import Blueprint
from utils.resp import responseto
from extensions.heartrate import band_init, reset_bluetooth

util = Blueprint('util', __name__)


@util.route('/util/initband')
def initband():
    cb = band_init()
    if cb == 'ok':
        return responseto(100)
    else:
        return responseto(213)


@util.route('/util/reset')
def reset():
    cb = reset_bluetooth()
    if cb == '':
        return responseto(100)
    else:
        return responseto(214)
