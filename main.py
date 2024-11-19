import cv2
import face_recognition
import sqlite3
from datetime import datetime
from database import initialize_database

# Function to mark attendance
def mark_attendance(attendance_database, student_data):
    conn = sqlite3.connect(attendance_database)
    cursor = conn.cursor()

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()

        # Load known face encodings from the database
        cursor.execute("SELECT name, face_encoding FROM students")
        known_face_encodings = []
        known_face_names = []
        for row in cursor.fetchall():
            name, encoding = row
            known_face_names.append(name)
            known_face_encodings.append(eval(encoding))

        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

                # Mark attendance for the recognized student with the current date
                current_date = datetime.now().strftime("%Y-%m-%d")
                cursor.execute("INSERT INTO attendance (name, date) VALUES (?, ?)",
                               (name, current_date))
                conn.commit()

            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    conn.close()

if __name__ == "__main__":
    # Create or connect to the database
    attendance_database = "attendance_database.db"
    initialize_database(attendance_database)

    # Student data with names and image file paths
    student_data = [
        {"name": "viraj", "image_path": "C:\\Users\\VIRAJ\\Desktop\\miniprojecct\\student_data\\viraj\\viraj.jpg"},
        {"name": "harsh", "image_path": "C:\\Users\\VIRAJ\\Desktop\\miniprojecct\\student_data\\harsh\\harsh.jpg"}
    ]

    # Load student data into the database
    conn = sqlite3.connect(attendance_database)
    cursor = conn.cursor()
    for student in student_data:
        # Load the image
        image = face_recognition.load_image_file(student["image_path"])
        # Encode the face features
        face_encoding = face_recognition.face_encodings(image)
        if face_encoding:
            # Store the encoded face and student information in the database
            encoded_face = str(face_encoding[0].tolist())
            cursor.execute("INSERT INTO students (name, student_id, face_encoding) VALUES (?, ?, ?)",
                           (student["name"], None, encoded_face))

    conn.commit()
    conn.close()

    # Mark attendance using images from a folder
    mark_attendance(attendance_database, student_data)
