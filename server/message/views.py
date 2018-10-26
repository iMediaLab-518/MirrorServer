from flask import Blueprint, current_app
from ..util import responseto

message_bp = Blueprint('message', __name__)


@message_bp.route('/message')
def message():
    if current_app.message.empty():
        mes = None
    else:
        mes = current_app.message.get()
    return responseto(100, mes)

