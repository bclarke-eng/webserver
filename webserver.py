from flask import Flask

app = Flask(__name__)


@app.route('/greet/<string:name>')
def hello(name):
    return f'Message in a bottle for {name}!'


if __name__ == '__main__':
    app.run(host='localhost', port='8080', debug=True)

