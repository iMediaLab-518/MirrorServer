from flask import Flask
from route.auth_route import auth
from route.extension_route import extension
from route.util_route import util

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(extension)
app.register_blueprint(util)

app.config['JSON_AS_ASCII'] = False  # 返回支持中文

if __name__ == '__main__':
    app.run(debug=True)
