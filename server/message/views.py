from flask import Blueprint, current_app, request
from ..util import responseto

message_bp = Blueprint('message', __name__)


@message_bp.route('/message', methods=["POST", "GET"])
def message():
    if request.method == 'GET':
        if current_app.message.empty():
            mes = None
        else:
            mes = current_app.message.get()
        return responseto(100, mes)
    elif request.method == 'POST':
        message = request.form['message']
        current_app.message.put(message)
        return responseto(100)
