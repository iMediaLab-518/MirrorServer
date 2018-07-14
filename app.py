from flask import Flask
from core.register import register
from core.login import login

app = Flask(__name__)


@app.route('/register/<person>')
def Register(person):
    register(person)


@app.route('/login')
def Login():
    return login()


if __name__ == '__main__':
    app.run()
