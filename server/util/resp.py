from flask.json import jsonify


def responseto(status, data=None):
    response = {
        'status': status,
        'out': data
    }
    resp = jsonify(response)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
