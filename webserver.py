import sqlite3
from flask import Flask, g

DATABASE = r'C:\libraltranary\library.db'

app = Flask(__name__)

# If we don't have a database connection already, we create a new one and attach it to the 'g' global object


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Close an open database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/greet/<string:name>')
def hello(name):
    return f'Message in a bottle for {name}!'


@app.route('/calculate/<int:num>')
def calculate(num):
    db = get_db()
    result = db.execute('select ? * ? * ?', (num, num, num)).fetchone()[0]
    # Fetchone returns a tuple so you need to index the first item (second item is empty)
    return f'The result is {result}!'


if __name__ == '__main__':
    app.run(host='localhost', port='8080', debug=True)

