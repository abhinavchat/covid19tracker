import os
class Config(object):
    BASE_URL = "https://api.covid19india.org/data.json"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "thisisaverysecretkey"
    DEBUG=False
    TESTING=False


class DevConfig(Config):
    DEBUG=True
    FLASK_ENV='development'


class TestConfig(Config):
    DEBUG=True
    TESTING=True

class ProdConfig(Config):
    pass


create_config = dict(dev=DevConfig, test=TestConfig, prod=ProdConfig)