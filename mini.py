import os
import env
from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm


app = Flask(__name__)


# SSSHHHH
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# @ BOTTOM BECAUSE OF CIRCULAR IMPORTS


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/')
def home():
    render_template('index.html', title='Home')


@app.route('/login')
def login():
    form = LoginForm()
    return  render_template('login.html', title='Log In', form=form)


if __name__ == '__main__':
            app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
