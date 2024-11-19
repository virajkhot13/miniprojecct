from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/attendance', methods=['GET', 'POST'])
def view_attendance():
    if request.method == 'POST':
        date = request.form['date']
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM attendance WHERE date = ?", (date,))
        results = cursor.fetchall()
        conn.close()
        return render_template('attendance.html', results=results)
    return render_template('search.html')

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('attendance_database.db')
    return g.db

@app.teardown_appcontext
def close_db(e):
    db = g.pop('db', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()
