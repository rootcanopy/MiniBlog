from flask import Flask, render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm
from app.models import User


app = Flask(__name__)

db = MongoEngine(app)
#db.init_app(app)
#login_manager = LoginManager(app)
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
    #if current_user.is_authenticated:
        #return redirect(url_for('index'))
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