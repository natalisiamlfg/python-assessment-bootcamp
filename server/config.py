class BaseConfig:
    TESTING = False
    SECRET_KEY = "change me"
    SQLALCHEMY_DATABSE_URI = 'sqlite:///./users.sqlite3'
    BUNDLE_ERRORS = True
    JWT_SECRET_KEY = 'lincoln'
    
class DevelopmentConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    TESTING = True
    pass
