from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, socket

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.debug = True
db = SQLAlchemy(app)
hostname = socket.gethostname()

@app.route('/')
def index():
    return 'Hello, from sunny %s!\n' % hostname

@app.route('/db')
def dbtest():
    try:
        db.create_all()
    except Exception as e:
        return "Database problem" + str(e) + '\n'
    return 'Database Connected from %s!\n' % hostname

if __name__ == '__main__':
    app.run()
