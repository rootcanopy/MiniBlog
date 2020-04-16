from flask import render_template
from app import app

@app.route('/')
@app.route('/base')
def base():
    user = {'username': 'Davie'}
    posts= [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return  render_template('base.html', title='Home', user=user)