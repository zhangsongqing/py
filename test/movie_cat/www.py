from application import app
from controllers.index import index_page
####只做路由注册
#将蓝图对象注册到app
app.register_blueprint(index_page,url_prefix='/ops/index')