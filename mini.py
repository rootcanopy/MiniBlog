import os
import env
from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm


app = Flask(__name__)


# SSSSHHHH
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")





@app.route('/')
def base():
    return render_template('base.html')


@app.route('/index')
def home():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # IF ITS RIGHT THE FIRST TIME
    if form.validate_on_submit():
        flash('Login success for user {}, remember_me{}'.format(
            form.username.data, form.remember_me.data))
        
        return redirect(url_for('home'))
    return render_template('login.html', title='Log In', form=form)


if __name__ == '__main__':
            app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
