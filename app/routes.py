from flask import render_template
from app import app

@app.route('/')
@app.route('/base')
def base():
    user = {'username': 'Davie'}
    return  render_template('base.html', title='Home', user=user)