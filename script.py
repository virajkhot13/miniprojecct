import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("students.db")

# Create a cursor
cursor = conn.cursor()

# Create a table to store student information and attendance records
cursor.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY,
                  name TEXT,
                  student_id TEXT,
                  face_encoding TEXT)''')

# Commit changes and close the connection
conn.commit()
conn.close()
