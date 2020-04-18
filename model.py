import os

from mini import login
from flask_login import UserMixin

"""

class User(UserMixin, db.Document):

    _id = ObjectId (primary_key=True)
    username = StringField (unique=True)
    email = StringField (unique=True)
    password = StringField (default=True)
    
    # REPR TELLS PYTHON HOW TO DEAL WITH OBJECTS OF THIS. CLASS
    def __repr__(self):
        return '<User {}>'.format(self.username)
"""
"""
 @login_manager.user_loader
def load_user(_id):
    return User.mongo.db.find(toInt(_id))
"""