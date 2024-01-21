import os

class Config(object):
    DEBUG = True
    TESTING = False
    
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

    # Silence the deprecation warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API settings
    API_PAGINATION_PER_PAGE = 10


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    # production config
    pass


def get_config(env=None):
    return DevelopmentConfig()