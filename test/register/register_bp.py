from flask import Blueprint

#申明一个蓝图对象
blueprint = Blueprint('blueprint',__name__)

#蓝图路由
@blueprint.route('/')
def index():
    return 'index'

#蓝图路由
@blueprint.route('/head')
def head():
    return 'head---register'
