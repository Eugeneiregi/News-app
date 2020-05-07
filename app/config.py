import os
class Config:
    API_KEY = os.environ.get("API_KEY")
    SECRET_KEY = os.environ.get("SECRET_KEY")

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    "development": DevConfig,
    "production": ProdConfig
}