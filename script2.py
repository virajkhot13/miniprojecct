import sqlite3

conn = sqlite3.connect("attendance_database.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
records = cursor.fetchall()

for record in records:
    print(record)

conn.close()
