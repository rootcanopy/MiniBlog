import os
#from pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect, request, url_for, flash, session

app = Flask(__name__)

#mongo = Pymongo(app)


# SSSSHHHH
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = "blog"
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


# WHEN BASE LOADS
@app.route('/')
@app.route('/index')
def index():
    if 'logged_in' in session:
        current_user = mongo.db.users.find_one({'name': session[
            'username'].title()})
        return render_template('index.html', title='Home',
                            current_user=current_user)
    else:
        render_template('index.html', title='Home')


# USER REGISTRATION
@app.route('/register', methods=['GET', 'POST'])
def register():
    #Function for handling the registration of users
    if 'logged_in' in session:  # Check is user already logged in
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():

        db_user = mongo.db.users
        db_user = users.find_one({'name': request.form['username'].title()})

        if db_user is None:
            hash_pass = generate_password_hash(request.form['password'])
            users.insert_one({'name': request.form['username'].title(),
                             'pass': hash_pass})
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect(url_for('index'))

        flash('Sorry, username already taken. Please try another.')
        return redirect(url_for('register'))
    return render_template('register.html', form=form, title="Register")


# USER LOGIN
@app.route('/login', methods=['GET', 'POST'])
def user_login():
    #Logic for handling the loggin in of users
    if 'logged_in' in session:  # Check is already logged in
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.users
        logged_in_user = user.find_one({
                                'name': request.form['username'].title()})

        if logged_in_users:
            if check_password_hash(logged_in_user['pass'],
                                   request.form['password']):
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('index'))
            flash('Sorry incorrect password!')
            return redirect(url_for('user_login'))
    return render_template('login.html', form=form, title='Login')
    

# USER LOGOUT
@app.route('/logout')
def logout():
    #POP THE SESSION
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
            app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
