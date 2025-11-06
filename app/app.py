import sqlite3
from flask import Flask, jsonify, g, render_template, request

app = Flask(__name__)
DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/messages", methods=['GET', 'POST'])
def messages():
    db = get_db()
    if request.method == 'POST':
        message = request.json['message']
        db.execute('INSERT INTO messages (content) VALUES (?)', [message])
        db.commit()
        return '', 204
    else:
        cur = db.execute('SELECT content FROM messages ORDER BY id DESC')
        messages = [row[0] for row in cur.fetchall()]
        return jsonify(messages)

if __name__ == "__main__":
    app.run(debug=True)
