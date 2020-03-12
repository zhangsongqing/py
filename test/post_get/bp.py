from flask import Blueprint,request

#申明一个蓝图对象
blueprint = Blueprint('blueprint',__name__)

#蓝图路由
@blueprint.route('/')
def index():
    return '"request:%s"%( request.method)'

#蓝图路由
@blueprint.route('/head')
def head():
    #return 'head'
    return '"request:%s"%( request.method)'

@blueprint.route('/get')
def get():
    var_a = request.args.get('a','imooc')
    print(var_a)
    return "request:%s,params:%s,var_a:%s"%( request.method,request.args,var_a )