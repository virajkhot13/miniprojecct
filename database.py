import sqlite3

def initialize_database(attendance_database):
    conn = sqlite3.connect(attendance_database)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                      (id INTEGER PRIMARY KEY,
                       name TEXT,
                       student_id TEXT,
                       face_encoding TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS attendance
                      (id INTEGER PRIMARY KEY,
                       name TEXT,
                       date TEXT)''')
    conn.commit()
    conn.close()

def insert_attendance(cursor, name, date):
    cursor.execute("INSERT INTO attendance (name, date) VALUES (?, ?)", (name, date))
