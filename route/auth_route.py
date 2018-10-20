from flask import Blueprint
from core.register import register
from core.login import login
from utils.resp import responseto

auth = Blueprint('auth', __name__)


@auth.route('/register/<username>')
def Register(username):
    try:
        register(username)
        return responseto(100)
    except:
        return responseto(201)


@auth.route('/login')
def Login():
    try:
        username = login()
        if username != []:
            return responseto(100, username)
        else:
            return responseto(301)
    except:
        return responseto(302)
