from ..controller.register import register
from ..controller.login import login
from ..util import responseto

from flask import Blueprint

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register/<username>')
def Register(username):
    try:
        register(username)
        return responseto(100)
    except:
        return responseto(201)


@auth_bp.route('/login')
def Login():
    try:
        username = login()
        if username != []:
            return responseto(100, username)
        else:
            return responseto(301)
    except:
        return responseto(302)
