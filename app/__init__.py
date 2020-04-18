from flask import Flask
from mongoengine import *
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from env import Config


app = Flask(__name__)
app.config.from_object(Config)
db = MongoEngine(app)
#db.init_app(app)
#login_manager = LoginManager(app)
#login_manager.init_app(app)

from app import routes, models