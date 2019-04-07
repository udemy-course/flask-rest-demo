from datetime import timedelta


class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_EXPIRATION_DELTA = timedelta(seconds=300)
    JWT_AUTH_URL_RULE = '/auth/login'


class TestingConfig(Config):
    JWT_AUTH_HEADER_PREFIX = 'FLASK'
    SECRET_KEY = "flask123"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(Config):
    JWT_AUTH_HEADER_PREFIX = 'FLASK'
    SECRET_KEY = "flask123"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/demo'


class ProductionConfig(Config):
    pass


app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
