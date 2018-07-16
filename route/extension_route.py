from flask import Blueprint
from extensions.humidity import get_humidity
from extensions.temperature import get_temperature
import json

extension = Blueprint('extension', __name__)


@extension.route('/humidity')
def humidity():
    try:
        res = get_humidity()
        return json.dumps({
            "status": 100,
            "out": res
        })
    except:
        return json.dumps({
            "status": 204
        })


@extension.route('/temperature')
def temperature():
    try:
        res = get_temperature()
        return json.dumps({
            "status": 100,
            "out": res
        })
    except:
        return json.dumps({
            "status": 203
        })
