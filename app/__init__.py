from flask import Flask
from mongoengine import *
from flask_mongoengine import MongoEngine
from flask_login import LoginManager


app = Flask(__name__)