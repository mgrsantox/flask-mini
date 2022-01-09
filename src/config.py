from os import environ, path

basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, '.env'))

# print(environ.get("DATABASE_URI"))
# print('sqlite://' + path.join(basedir, 'flask_mini.db'))


class Config(object):

    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'flask_mini.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'flask_mini.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # DB_NAME = "pro_db"
    # DB_USERNAME = "admin"
    # DB_PASSWORD = "admin@123"

    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    # DB_NAME = "flask_db"

    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True

    SESSION_COOKIE_SECURE = False
