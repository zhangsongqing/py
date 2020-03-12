from mutil_resp import app
from blueprint_01 import blueprint
####只做路由注册
#将蓝图对象注册到app
app.register_blueprint(blueprint,url_prefix='/imooc')