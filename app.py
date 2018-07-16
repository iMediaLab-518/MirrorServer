from flask import Flask
from route.auth_route import auth
from route.extension_route import extension

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(extension)

if __name__ == '__main__':
    app.run(debug=True)
