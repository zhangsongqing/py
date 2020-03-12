from flask import Flask
from bp import blueprint
app = Flask(__name__)

#将蓝图对象注册到app
app.register_blueprint(blueprint,url_prefix='/imooc')

if __name__ == '__main__':
    app.run(debug=True)