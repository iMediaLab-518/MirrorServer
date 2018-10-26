from flask import Blueprint, request, session

from ..controller.humidity import get_humidity
from ..controller.temperature import get_temperature
from ..controller.heartrate import get_heartrate
from ..controller.weather import get_weather
from ..controller.weight import get_weight
from ..controller.traveladvice import get_travel_advice
from ..controller.news import get_news
from ..controller.pm25 import get_pm25
from ..controller.wind import get_wind

import random
from datetime import date, datetime

from ..util import responseto
from ..models import db, Heartrate, Weight

extension_bp = Blueprint('extension', __name__)


@extension_bp.route('/humidity')
def humidity():
    try:
        res = get_humidity()
        return responseto(100, res)
    except:
        return responseto(204)


@extension_bp.route('/temperature')
def temperature():
    try:
        res = get_temperature()
        return responseto(100, res)
    except:
        return responseto(203)


@extension_bp.route('/heartrate')
def heartrate():
    try:
        res = get_heartrate()
        if res != 'error' and res.strip():
            heartrate = Heartrate(time=datetime.now(), heartrate=res)
            db.session.add(heartrate)
            db.session.commit()
            return responseto(100, res)
        else:
            return responseto(206)
    except:
        return responseto(206)


@extension_bp.route('/weight')
def weight():
    try:
        res = get_weight()
        name = session['name']
        w = float(res.split(' ')[0])
        weight = Weight(name=name, weight=w, date=date.today())
        Weight.query.filter(Weight.date == date.today()).delete()
        db.session.add(weight)
        db.session.commit()
        return responseto(100, res)
    except:
        return responseto(205)


@extension_bp.route('/traveladvice')
def traveladvice():
    temperature = request.args.get('t')

    if temperature is None:
        temperature = random.randint(-11, 41)

    if isinstance(temperature, str):
        try:
            temperature = int(temperature)
        except:
            return responseto(208)

    res = get_travel_advice(temperature)
    return responseto(100, res)


@extension_bp.route('/news')
def news():
    try:
        res = get_news()
        return responseto(100, res)
    except:
        return responseto(209)


@extension_bp.route('/pm25')
def pm25():
    try:
        res = get_pm25()
        return responseto(100, res)
    except:
        return responseto(210)


@extension_bp.route('/weather')
def weather():
    try:
        res = get_weather()
        return responseto(100, res)
    except:
        return responseto(211)


@extension_bp.route('/wind')
def wind():
    try:
        res = get_wind()
        return responseto(100, res)
    except:
        return responseto(212)
