from ..controller.register import register
from ..controller.login import login
from ..util import responseto
from ..models import User, db
from flask import Blueprint, render_template, request

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['GET', 'POST'])
def Register():
    try:
        name = request.form['name']
        year = int(request.form['year'])
        gender = request.form['gender']
        height = int(request.form['height'])
        register(name)
        user = User(
            name=name,
            year=year,
            gender=gender,
            height=height
        )
        db.session.add(user)
        db.session.commit()
        return responseto(100)
    except:
        return responseto(201)


@auth_bp.route('/login')
def Login():
    try:
        name = login()
        if name != []:
            user = User.query.filter_by(name=name).first()
            return responseto(100, user.serialize())
        else:
            return responseto(301)
    except:
        return responseto(302)