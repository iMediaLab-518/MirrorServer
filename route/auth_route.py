import json

from flask import Blueprint
from core.register import register
from core.login import login

auth = Blueprint('auth', __name__)


@auth.route('/register/<username>')
def Register(username):
    try:
        register(username)
        return json.dumps({
            "status": 100
        })
    except:
        return json.dumps({
            "status": 201
        })


@auth.route('/login')
def Login():
    try:
        username = login()
        if username != []:
            return json.dumps({
                "status": 100,
                "out": username
            })
        else:
            return json.dumps({
                "status": 301
            })
    except:
        return json.dumps({
            "status": 202
        })
