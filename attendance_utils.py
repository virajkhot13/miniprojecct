import sqlite3
from datetime import datetime
import face_recognition
import cv2
from database import insert_attendance

def mark_attendance(attendance_database, student_data, known_faces):
    conn = sqlite3.connect(attendance_database)
    cursor = conn.cursor()

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()

        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_faces, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = student_data[first_match_index]["name"]

                # Mark attendance for the recognized student with the current date
                current_date = datetime.now().strftime("%Y-%m-%d")
                insert_attendance(cursor, name, current_date)
                conn.commit()

            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
