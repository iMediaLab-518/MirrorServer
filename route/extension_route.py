from flask import Blueprint, request
from extensions.humidity import get_humidity
from extensions.temperature import get_temperature
from extensions.heartrate import get_heartrate
from extensions.weight import get_weight
from extensions.traveladvice import get_travel_advice
import random

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


@extension.route('/heartrate')
def heartrate():
    try:
        res = get_heartrate()
        return json.dumps({
            "status": 100,
            "out": res
        })
    except:
        return json.dumps({
            "status": 206
        })


@extension.route('/weight')
def weight():
    try:
        res = get_weight()
        return json.dumps({
            'status': 100,
            "out": res
        })
    except:
        return json.dumps({
            "status": 205
        })


@extension.route('/traveladvice')
def traveladvice():
    temperature = request.args.get('t')

    if temperature is None:
        temperature = random.randint(-11, 41)

    if isinstance(temperature, str):
        try:
            temperature = int(temperature)
        except:
            return json.dumps({
                "status": 208
            })

    res = get_travel_advice(temperature)
    return json.dumps({
        "status": 100,
        "out": res
    }, ensure_ascii=False)
