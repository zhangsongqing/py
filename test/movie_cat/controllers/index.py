from flask import Blueprint,render_template
from sqlalchemy import text
from application import db

#申明一个蓝图对象
index_page = Blueprint('index_page',__name__)

@index_page.route('/')
def index():
    dict = {'name':'b'}
    sql = text('select user from `user`;')
    result = db.engine.execute(sql)
    print(result)
    dict['mysql_user'] = result
    dict['user'] = {'name':'zsq','age':2666666663,'addr':'安徽省'}
    dict['number_list'] = [1,2,3,4,5]
    #可以传递一个字典（可以是元组，可以是字典）
    return render_template('index2.html',**dict)




