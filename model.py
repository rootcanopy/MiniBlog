from datetime import datetime
import os
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from mini import login
from flask_mongoengine.wtf import model_form, Document
from flask_login import UserMixin


"""
@login_manager.user_loader
def load_user(_id):
    return User.mongo.db.find(toInt(_id))
"""

class User(UserMixin, db.Document):
    _id = db.IntField (primary_key=True)
    username = db.StringField (max_length=50, required=True)
    email = db.EmailField(max_length=50, required=True)
    image_file = db.ImageField(default='default.jpg')
    password_hash = db.PasswordField (default=True)
    posts = db.ReferenceField ('User', backref='author', lazy='dynamic')
    
    # REPR TELLS PYTHON HOW TO DEAL WITH OBJECTS OF THIS. CLASS
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self.password_hash, password)


class Post(db.Document):
    _id = db.IntField (primary_key=True)
    title = db.StringField (max_length=120,required=True)
    author = db.ReferenceField(User)
    date_posted = db.DateTimeField (index=True, default=datetime.utcnow)
    content = db.TextAreaField(max_length=200)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
