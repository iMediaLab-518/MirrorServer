from flask import Blueprint
from core.register import register
from core.login import login

auth = Blueprint('auth', __name__)


@auth.route('/register/<username>')
def Register(username):
    register(username)


@auth.route('/login')
def Login():
    return login()
