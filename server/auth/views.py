from ..controller.register import register
from ..controller.login import login
from ..util import responseto
from ..models import User, db
from flask import Blueprint, request, session, current_app

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['GET', 'POST'])
def Register():
    try:
        name = request.form['name']
        year = int(request.form['year'])
        gender = request.form['gender']
        height = int(request.form['height'])
        current_app.message.put('register')
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
        current_app.message.put('login')
        name = login()
        if name != []:
            user = User.query.filter_by(name=name).first()
            session['user'] = user
            return responseto(100, user.serialize())
        else:
            return responseto(301)
    except:
        return responseto(302)


@auth_bp.route('/logout')
def Logout():
    session.pop('user')
    return responseto(100)
