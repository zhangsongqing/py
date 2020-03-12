#####jinja2模板
    1.if判断
        dict['user'] = {'name':'zsq','age':23,'addr':'安徽省'}
        
        {% if user %}
            姓名：{{ user.name }},年龄：{{ user.age }},住址：{{ user.addr }}
        {% endif %}
        
    2.for循环
        dict['number_list'] = [1,2,3,4,5]
        
        {% for temp in number_list %}
            {{temp}}
        {% endfor %}
        
    3.模板继承
        1.定义公共模块layout.html
            {% block context %} {%endblock%}
        2.在entend_template.html中引入公共模块
            <!--引入公共模块-->
            {% extends "common/layout.html" %}
        3.访问
        @blueprint.route('/entend_template')
            def extend_template():
            return render_template('extend_template.html')
        
