import os

class Config():
 SECRET_KEY = os.environ.get('SECRET_KEY')
 SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
 SQLALCHEMY_TRACK_MODIFICATIONS = False

 MAIL_SERVER = 'smtp.googlemail.com'
 MAIL_PORT = 587
 MAIL_USE_TLS = True
 MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
 MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")



class DevConfig(Config):
    #SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://nancy:AAaa11..@localhost/pitch'
    DEBUG = True

class ProdConfig(Config):
    DEBUG=False

config_options = {
"dev":DevConfig,
"prod":ProdConfig
}


MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")