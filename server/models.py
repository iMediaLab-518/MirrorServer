from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    gender = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return [self.name, self.gender, self.year, self.height]

    @property
    def age(self):
        return date.today().year - self.year

    @property
    def MH1(self):
        return (205.8 - 0.685 * self.age) * 0.7

    @property
    def MH2(self):
        return (205.8 - 0.685 * self.age) * 0.6


class Weight(db.Model):
    __tablename__ = 'weight'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    weight = db.Column(db.Float)
    date = db.Column(db.Date)


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

    def serialize(self, male):
        if male:
            strength = self.strength_male
        else:
            strength = self.strength_female
        return [self.id, self.title, self.level, strength, self.length]


class Record(db.Model):
    __tablename__ = 'record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    time = db.Column(db.DateTime)
    v_id = db.Column(db.Integer, db.ForeignKey('video.id'))
