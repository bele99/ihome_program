# coding:utf-8

import redis
import logging
from logging.handlers import RotatingFileHandler
from ihome.utils.commons import ReConverter

from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect


# Database
db= SQLAlchemy()

# Create a redis connection object
redis_store = None

# Log information
logging.basicConfig(level=logging.DEBUG)
# Create a logger. Set the path for saving logs, the maximum size of each log file, and the maximum number of saved log files.
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# Create a format for logging
# Log level, Input file name, Number of lines, Log information
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# Set the logging format for the newly created logger.
file_log_handler.setFormatter(formatter)
# Used by the flask app
logging.getLogger().addHandler(file_log_handler)
# Set the logging level for logs
logging.basicConfig(level=logging.DEBUG)  # debug


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

    # Add a custom converter for flask
    app.url_map.converters["re"] = ReConverter

    # Blueprint for Registration (version)
    from ihome import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1.0")

    # Register to provide a blueprint for static files (web_html)
    from ihome import web_html
    app.register_blueprint(web_html.html)

    return app