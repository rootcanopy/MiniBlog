"""
from datetime import datetime
from flask_mongoengine.wtf import model_form, Document
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from mini import login_manager

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

    # ENCRYPTING USER PASSWORDS
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id)first()


class Post(db.Document):
    _id = db.IntField (primary_key=True)
    title = db.StringField (max_length=120,required=True)
    author = db.ReferenceField(User)
    date_posted = db.DateTimeField (index=True, default=datetime.utcnow)
    content = db.TextAreaField(max_length=200)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
"""