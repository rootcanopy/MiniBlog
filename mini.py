import os
import env

from flask import Flask, render_template, url_for, flash, redirect
from flask_mongoengine import MongoEngine
from flask_login import login_user
from forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
#from models import User


app = Flask(__name__)


# SSSSHHHH
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = "blog"

db = MongoEngine(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
#login_manager = LoginManager()
#login_manager.init_app(app)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/index')
def home():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    #IF SESSION ACTIVE IN BROWSER
    if current_user.is_authenticated == True:
        return redirect(url_for('index'))
    form = LoginForm()

    # IF ITS RIGHT THE FIRST TIME
    if form.validate_on_submit():
        existing_u = User.objects(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):

            flash(f'Invalid username or password')
            return redirect(url_for('login'))
            #flash('Login success for user {}, remember_me{}'.format(
            #form.username.data, form.remember_me.data))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template('login.html', title='Log In', form=form)


if __name__ == '__main__':
            app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
