from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

# Database setup
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS livestock (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        genetic_traits TEXT,
        health_status TEXT,
        productivity TEXT
    )''')
    conn.commit()
    conn.close()

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        name = request.form['name']
        genetic_traits = request.form['genetic_traits']
        health_status = request.form['health_status']
        productivity = request.form['productivity']

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO livestock (name, genetic_traits, health_status, productivity) VALUES (?, ?, ?, ?)",
            (name, genetic_traits, health_status, productivity)
        )
        conn.commit()
        conn.close()

        return redirect(url_for('recommendations'))
    return render_template('upload.html')

@app.route('/recommendations')
def recommendations():
    conn = get_db_connection()
    data = conn.execute("SELECT * FROM livestock").fetchall()
    conn.close()

    # Example recommendation logic (basic matching)
    recommendations = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i]['genetic_traits'] == data[j]['genetic_traits']:
                recommendations.append((data[i], data[j]))

    return render_template('recommendations.html', data=data, recommendations=recommendations)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    conn = get_db_connection()

    if request.method == 'POST':
        name = request.form['name']
        genetic_traits = request.form['genetic_traits']
        health_status = request.form['health_status']
        productivity = request.form['productivity']

        conn.execute("""
            UPDATE livestock
            SET name = ?, genetic_traits = ?, health_status = ?, productivity = ?
            WHERE id = ?
        """, (name, genetic_traits, health_status, productivity, id))
        conn.commit()
        conn.close()

        return redirect(url_for('recommendations'))

    livestock = conn.execute("SELECT * FROM livestock WHERE id = ?", (id,)).fetchone()
    conn.close()
    return render_template('update.html', livestock=livestock)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)