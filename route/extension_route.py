from flask import Blueprint, request

from extensions.humidity import get_humidity
from extensions.temperature import get_temperature
from extensions.heartrate import get_heartrate
from extensions.weather import get_weather
from extensions.weight import get_weight
from extensions.traveladvice import get_travel_advice
from extensions.news import get_news
from extensions.pm25 import get_pm25
import random

from extensions.wind import get_wind
from utils.resp import responseto

extension = Blueprint('extension', __name__)


@extension.route('/humidity')
def humidity():
    try:
        res = get_humidity()
        return responseto({
            "status": 100,
            "out": res
        })
    except:
        return responseto({
            "status": 204
        })


@extension.route('/temperature')
def temperature():
    try:
        res = get_temperature()
        return responseto({
            "status": 100,
            "out": res
        })
    except:
        return responseto({
            "status": 203
        })


@extension.route('/heartrate')
def heartrate():
    try:
        res = get_heartrate()
        return responseto({
            "status": 100,
            "out": res
        })
    except:
        return responseto({
            "status": 206
        })


@extension.route('/weight')
def weight():
    try:
        res = get_weight()
        return responseto({
            'status': 100,
            "out": res
        })
    except:
        return responseto({
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
            return responseto({
                "status": 208
            })

    res = get_travel_advice(temperature)
    return responseto({
        "status": 100,
        "out": res
    })


@extension.route('/news')
def news():
    try:
        res = get_news()
        return responseto({
            "status": 100,
            "out": res
        })
    except:
        return responseto({
            "status": 209
        })


@extension.route('/pm25')
def pm25():
    try:
        res = get_pm25()
        return responseto({
            "status": 100,
            "out": res
        })
    except:
        return responseto({
            "status": 210
        })


@extension.route('/weather')
def weather():
    try:
        res = get_weather()
        return responseto({
            "status": 100,
            "out": res
        })
    except:
        return responseto({
            "status": 211
        })


@extension.route('/wind')
def wind():
    try:
        res = get_wind()
        return responseto({
            "status": 100,
            "out": res
        })
    except:
        return responseto({
            "status": 212
        })
