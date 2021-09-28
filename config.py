import os

class Config():
 SECRET_KEY = os.environ.get('SECRET_KEY')
 SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
 SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    #SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://nancy:AAaa11..@localhost/pitch'
    DEBUG = True

class ProdConfig(Config):
    DEBUG=False

config_options = {
"dev":DevConfig,
"prod":ProdConfig
}
