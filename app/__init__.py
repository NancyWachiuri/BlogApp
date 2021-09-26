from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app