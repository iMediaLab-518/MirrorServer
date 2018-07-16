from flask import Blueprint
from extensions.humidity import get_humidity
from extensions.temperature import get_temperature
import json

extension = Blueprint('extension', __name__)


@extension.route('/humidity')
def humidity():
    return get_humidity()


@extension.route('/temperature')
def temperature():
    return get_temperature()
