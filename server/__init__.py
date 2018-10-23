from flask import Flask

from .auth import auth_bp
from .extensions import extension_bp
from .bluetooth import bluetooth_bp
from .models import db, User

app = Flask(__name__)


def init_app(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(extension_bp)
    app.register_blueprint(bluetooth_bp)

    app.config['JSON_AS_ASCII'] = False  # 返回支持中文
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    db.create_all(app=app)
    return app


app = init_app(app)
