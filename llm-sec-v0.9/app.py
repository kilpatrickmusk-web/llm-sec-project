#启动flask

from flask import Flask
from routes import register_all_routes
from config import Config



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    #注册所有路由
    register_all_routes(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True,port=8888)