from flask import Blueprint,request

#申明一个蓝图对象
blueprint = Blueprint('blueprint',__name__)

#蓝图路由
@blueprint.route('/')
def index():
    return "request:%s"%( request.method)

#蓝图路由
@blueprint.route('/head')
def head():
    #return 'head'
    return "request:%s"%( request.method)

@blueprint.route('/get')
def get():
    #变种
    req = request.values
    var_a = req['a'] if 'a' in req else 'req_a'
    #var_a = request.args.get('a') if 'a' in request.args else 'aaa'
    print(var_a)
    return "request:%s,params:%s,var_a:%s"%( request.method,request.args,var_a )

@blueprint.route('/post',methods = ['post'])
def post():
    #var_a = request.form['a'] if 'a' in request.form else 'aaa'
    req = request.values
    var_a = req['a'] if 'a' in req else 'req_a'
    dict = {}
    dict.update(a='b',c='d')
    import json
    js = json.dumps(dict,indent=4,ensure_ascii='')
    return "req:%s,request:%s,params:%s,var_a:%s,dict:%s,\njs:%s"%(req,request.method,request.form,var_a,dict,js)

@blueprint.route('/upload',methods = ['post'])
def upload():
    req = request.files
    var_a = req['file'] if 'file' in req else None
    return "request:%s,params:%s,var_a:%s"%(request.method,req,var_a)
