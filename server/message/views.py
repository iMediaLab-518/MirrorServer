from flask import Blueprint, current_app, request
from ..util import responseto

message_bp = Blueprint('message', __name__)


# Message Queue
# @message_bp.route('/message', methods=["POST", "GET"])
# def message():
#     if request.method == 'GET':
#         if current_app.message.empty():
#             mes = None
#         else:
#             mes = current_app.message.get()
#         return responseto(100, mes)
#     elif request.method == 'POST':
#         message = request.form['message']
#         current_app.message.put(message)
#         return responseto(100)


@message_bp.route('/message', methods=["POST", "GET"])
def message():
    if request.method == 'GET':
        return responseto(100, current_app.messages)
    elif request.method == 'POST':
        for k, v in request.form.items():
            if v.upper() == 'TRUE':
                current_app.messages[k] = True
            else:
                current_app.messages[k] = False
        return responseto(100)
