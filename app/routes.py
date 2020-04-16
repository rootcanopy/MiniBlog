from flask import render_template
from app import app
from app.forms import LoginForm


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
