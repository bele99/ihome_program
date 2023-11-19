# coding:utf-8


class Config(object):
    """Configuration information"""
    SECRET_KEY = "XHSOI*Y9dfs9cshd9"

    # Database
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_python04"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask-session Configuration
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # The session_id in the cookie is hidden
    PERMANENT_SESSION_LIFETIME = 86400 # Duration of session data in seconds


class DevelopmentConfig(Config):
    ''' Development model configuration information'''
    DEBUT = True
    pass

class ProductionConfig(Config):
    ''' Production model configuration information'''
    pass

config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}