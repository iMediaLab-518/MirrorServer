from flask import Flask
from core.register import register

app = Flask(__name__)


@app.route('/register/<person>')
def hello_world(person):
    register(person)


if __name__ == '__main__':
    app.run()
