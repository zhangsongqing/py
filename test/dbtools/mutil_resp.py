from flask import Flask
from flask_sqlalchemy import SQLAlchemy

##核心对象初始化
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://wxgz:Gdzq_Infobeat_2019@172.10.4.100/mysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
