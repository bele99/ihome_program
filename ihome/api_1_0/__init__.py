# coding:utf-8

from flask import Blueprint

# create blueprints
api = Blueprint("api_1_0", __name__)

# load the view of blueprint
from . import index