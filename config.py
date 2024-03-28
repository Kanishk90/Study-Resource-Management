class Config(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLAlchemy_DATABASE_URI = "sqlite///dev.db"