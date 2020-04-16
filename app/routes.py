from app import app

@app.route('/')
@app.route('/base')
def base():
    return