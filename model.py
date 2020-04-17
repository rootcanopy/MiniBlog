import mini
from flask_login import UserMixin


class User(UserMixin, db.Document):

    _id = ObjectId (primary_key=True)
    username = StringField (unique=True)
    email = StringField (unique=True)
    password = StringField (default=True)
    
    # REPR TELLS PYTHON HOW TO DEAL WITH OBJECTS OF THIS. CLASS
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    