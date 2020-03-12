from flask import Blueprint,request,render_template

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
    var_a = req['a'] if 'a' in req else 'req_assssssssssssssss'
    #var_a = request.args.get('a') if 'a' in request.args else 'aa-------a'
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


#参数传递到html
@blueprint.route('/index1')
def index1():
    name = 'zsq'
    return render_template('index.html',name=name)

    #url_for():func
    #蓝图.func
#蓝图路由
@blueprint.route('/index2')
def index2():
    dict = {}
    dict = {'name':'b'}
    #可以传递一个字典（可以是元组，可以是字典）
    return render_template('index2.html',**dict)

@blueprint.route('/template_mode')
def template_mode():
    dict = {'name':'b'}
    dict['user'] = {'name':'zsq','age':23333,'addr':'安徽省'}
    dict['number_list'] = [1,2,3,4,5]
    #可以传递一个字典（可以是元组，可以是字典）
    return render_template('index2.html',**dict)


@blueprint.route('/entend_template')
def extend_template():
    return render_template('extend_template.html')
