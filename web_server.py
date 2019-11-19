from flask import Flask, render_template, url_for
web_server = Flask(__name__)


@web_server.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    web_server.run(debug=True)