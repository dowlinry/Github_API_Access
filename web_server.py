from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

web_server = Flask(__name__)
web_server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(web_server)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)

@web_server.route('/')
def index():
    return render_template('index.html')

if  __name__ == '__main__':
    web_server.run(debug=True)
