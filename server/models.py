from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    name = db.Column(db.String, primary_key=True)
    gender = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return [self.name, self.gender, self.year, self.height]


class Weight(db.Model):
    __tablename__ = 'weight'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    weight = db.Column(db.Float)
    date = db.Column(db.DateTime)


class Heartrate(db.Model):
    __tablename__ = 'heartrate'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime)
    heartrate = db.Column(db.Integer)


class Video(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    level = db.Column(db.Integer)
    strength_male = db.Column(db.Float)
    strength_female = db.Column(db.Float)
    length = db.Column(db.Integer)


class Record(db.Model):
    __tablename__ = 'record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    time = db.Column(db.DateTime)
    v_id = db.Column(db.Integer, db.ForeignKey('video.id'))
