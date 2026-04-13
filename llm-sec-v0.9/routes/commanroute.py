from flask import render_template

def  register_routes(app)->None:
    
    @app.route('/')
    def home():
        return render_template('index.html')##render_template():只会在templates文件夹中找.html文件
    
    @app.route('/greet/<name>',methods=['GET'])#<name>:路由参数,可以通过url传递参数给函数（获取url中的?name=xxx），使用GET方法传递
    def greet(name):
        return f'Hello, {name}!'

    
    
    

    