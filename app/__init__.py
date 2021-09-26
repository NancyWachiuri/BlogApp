from flask import Flask
#from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy

#bootstrap = Bootstrap()
db = SQLAlchemy()
def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(config_options[config_name])
    db.init_app(app)

   # bootstrap.init_app(app)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    return app