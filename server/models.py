from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    name = db.Column(db.String, primary_key=True)
    gender = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return [self.name, self.gender, self.year, self.height]
