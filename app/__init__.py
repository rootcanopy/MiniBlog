from flask import flask

app = Flask(__name__)

# @ BOTTOM BECAUSE OF CIRCULAR IMPORTS
from app import routes