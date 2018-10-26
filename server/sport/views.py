from datetime import datetime

from flask import Blueprint, current_app
from sqlalchemy import func

from ..models import *
from ..util import responseto

sport_bp = Blueprint('sport', __name__)


@sport_bp.route('/sport/warmup')
def warmup():
    warmup_video = Video.query.filter(Video.level == 0).first()
    user = current_app.user

    record = Record(name=user.name, time=datetime.now(), v_id=warmup_video.id)
    db.session.add(record)
    db.session.commit()

    return responseto(100, warmup_video.serialize(user.gender == '男'))


@sport_bp.route('/sport/start')
def start():
    avg_heartrate = db.session.query(func.avg(Heartrate.heartrate)).first()[0]
    user = current_app.user

    min_h = 80
    max_h = user.MH1

    videos = Video.query.filter(Video.level > 0).all()
    videos.sort(key=lambda v: v.strength_male)
    interval = (max_h - min_h) / (len(videos) - 2)

    h = min_h
    for video in videos:
        if avg_heartrate <= h:
            ans_video = video
            break
        h += interval
    else:
        ans_video = videos[-1]
    record = Record(name=user.name, time=datetime.now(), v_id=ans_video.id)
    db.session.add(record)
    db.session.commit()

    return responseto(100, ans_video.serialize(user.gender == '男'))


@sport_bp.route('/sport/sport_times')
def sport_times():
    user = current_app.user
    times = len(Record.query.filter(Record.name == user.name).all())
    return responseto(100, times)


@sport_bp.route('/sport/calorie')
def calorie():
    user = current_app.user
    record = Record.query.filter(Record.name == user.name).sort_by(Record.time.desc()).first()
    video = Video.query.filter(Video.id == record.v_id).first()
    weight = Weight.query.filter(Weight.name == user.name).sort_by(Weight.date.desc()).first()

    w = weight.weight
    length = video.length
    if user.gender == '男':
        strength = video.strength_male
    else:
        strength = video.strength_female
    return responseto(100, strength * w * length / 3600)
