import os
import env
from flask_login import LoginManager, current_user, login_user
from flask import Flask, render_template, url_for, flash, redirect
from flask_pymongo import PyMongo
from forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)


# SSSSHHHH
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


mongo = PyMongo(app)
login_manager = LoginManager(app)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/index')
def home():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    # IF ITS RIGHT THE FIRST TIME
    if form.validate_on_submit():
        user = User.mongo.db.find_one(username=form.username.data).first_or_404()
        if user is None or not user.check_password(form.password.data):
            flash(f'Invalid username or password')
            return redirect(url_for('home'))
            #flash('Login success for user {}, remember_me{}'.format(
            #form.username.data, form.remember_me.data))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template('login.html', title='Log In', form=form)


if __name__ == '__main__':
            app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
