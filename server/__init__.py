from queue import Queue

from flask import Flask
from flask_session import Session
from .auth import auth_bp
from .extensions import extension_bp
from .bluetooth import bluetooth_bp
from .data import data_bp
from .sport import sport_bp
from .message import message_bp
from .models import db, User

app = Flask(__name__)


def init_app(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(extension_bp)
    app.register_blueprint(bluetooth_bp)
    app.register_blueprint(data_bp)
    app.register_blueprint(sport_bp)
    app.register_blueprint(message_bp)

    app.config['secret_key'] = b'_5#y2L"F4Q8z\n\xec]/'

    app.config['JSON_AS_ASCII'] = False  # 返回支持中文
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.message = Queue()
    app.user = None

    db.init_app(app)
    db.create_all(app=app)
    return app


app = init_app(app)
