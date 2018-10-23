
from ..util import responseto
from ..controller.heartrate import band_init, reset_bluetooth

from flask import Blueprint

bluetooth_bp = Blueprint('bluetooth', __name__)


@bluetooth_bp.route('/util/initband')
def initband():
    cb = band_init()
    if cb == 'ok':
        return responseto(100)
    else:
        return responseto(213)


@bluetooth_bp.route('/util/reset')
def reset():
    cb = reset_bluetooth()
    if cb == '':
        return responseto(100)
    else:
        return responseto(214)
