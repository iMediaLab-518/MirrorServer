from flask import Flask
from route.auth_route import auth
from route.extension_route import extension

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(extension)

app.config['JSON_AS_ASCII'] = False # 返回支持中文

if __name__ == '__main__':
    app.run(debug=True)
