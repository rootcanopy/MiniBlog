import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    os.environ['SECRET_KEY'] = '8bf1555c499fe3cc55021fd1e87585e5'

    os.environ["MONGO_URI"] = "mongodb+srv://rootcanopy:Di1LJQyxmTBKIvCj@mycluster-t6yqh.mongodb.net/blog?retryWrites=true&w=majority"

    os.environ["PORT"] = "5000"

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False