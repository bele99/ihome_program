# coding:utf-8

from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_seesion import Session
from flask_wtf import CSRFProtect
from ihome import api_1_0

import redis

# Database
db= SQLAlchemy()


# Create a redis connection object
redis_store = None

#Factory model
def create_app(config_name):
    """
    Create an application object for flask
    : param config_name: str The name of the configuration mode ("develop", "product")
    : return:
    """

    app = Flask(__name__)

    # Get the class of the parameter based on the name of the configuration pattern
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    #Initialize database with app
    db.init_app(app)

    #Initialize redis
    global redis_store
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # Save session data to redis using flask-session
    Session(app)

    # Adding csrf protection to flask
    CSRFProtect(app)

    # Blueprint for Registration
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1.0")

    return app