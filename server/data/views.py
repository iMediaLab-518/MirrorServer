from flask import Blueprint, session, request
from ..util import responseto
from ..models import *
from sqlalchemy import func
from datetime import date

data_bp = Blueprint("data", __name__)


@data_bp.route('/data/BMI')
def bmi():
    user = session['user']
    height = user.height
    w = Weight.query.filter(Weight.name == user.name).order_by(Weight.date.desc()).first().weight
    return responseto(100, w / height * 100 / height * 100)


@data_bp.route('/data/max_heartrate')
def max_heartrate():
    heartrate = db.session.query(func.max(Heartrate.heartrate)).first()
    return responseto(100, heartrate[0])


@data_bp.route('/data/avg_heartrate')
def avg_heartrate():
    heartrate = db.session.query(func.avg(Heartrate.heartrate)).first()
    return responseto(100, heartrate[0])


@data_bp.route('/data/clear_heartrate')
def clear_heartrate():
    Heartrate.query.delete()
    db.session.commit()
    return responseto(100)


@data_bp.route('/data/MH2')
def MH2():
    user = session['user']
    return responseto(100, user.MH2)


@data_bp.route('/data/MH1')
def MH1():
    user = session['user']
    return responseto(100, user.MH1)


@data_bp.route('/data/weight')
def get_weight():
    text = request.args['text']
    user = session['user']
    name = user.name
    weight = Weight.query.filter(Weight.name == name and Weight.date == text).first().weight
    return responseto(100, weight)


@data_bp.route('/data/height')
def get_height():
    user = session['user']
    return responseto(100, user.height)
