import env
from flask import Flask


app = Flask(__name__)


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# @ BOTTOM BECAUSE OF CIRCULAR IMPORTS
from app import routes