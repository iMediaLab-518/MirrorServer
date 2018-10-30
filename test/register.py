import requests


def register():
    url = "http://localhost:5000/register"
    data = {
        'name': '王熠',
        'gender': '男',
        'height': 190,
        'year': 1998
    }
    requests.post(url, data=data)


if __name__ == '__main__':
    register()
