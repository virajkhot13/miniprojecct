import face_recognition
import sqlite3

def load_known_faces(attendance_database):
    conn = sqlite3.connect(attendance_database)
    cursor = conn.cursor()

    cursor.execute("SELECT face_encoding FROM students")
    known_face_encodings = [eval(encoding) for (encoding,) in cursor.fetchall()]

    conn.close()
    return known_face_encodings
