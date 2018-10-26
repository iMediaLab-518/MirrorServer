from flask import Flask
from flask_session import Session
from .auth import auth_bp
from .extensions import extension_bp
from .bluetooth import bluetooth_bp
from .data import data_bp
from .models import db, User

app = Flask(__name__)


def init_app(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(extension_bp)
    app.register_blueprint(bluetooth_bp)
    app.register_blueprint(data_bp)

    app.config['secret_key'] = b'_5#y2L"F4Q8z\n\xec]/'

    app.config['JSON_AS_ASCII'] = False  # 返回支持中文
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.config['SESSION_TYPE'] = 'sqlalchemy'  # session类型为sqlalchemy
    app.config['SESSION_SQLALCHEMY'] = db  # SQLAlchemy对象
    app.config['SESSION_SQLALCHEMY_TABLE'] = 'session'  # session要保存的表名称
    app.config['SESSION_PERMANENT'] = True  # 如果设置为True，则关闭浏览器session就失效。
    app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
    app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀

    Session(app)
    db.init_app(app)
    db.create_all(app=app)
    return app


app = init_app(app)
