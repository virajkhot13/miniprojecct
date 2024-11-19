import cv2
from datetime import datetime
from attendance_utils import mark_attendance
from database import initialize_database
from face_recognition_util import load_known_faces


if __name__ == "__main__":
    attendance_database = "attendance_database.db"
    initialize_database(attendance_database)

    student_data = [
        {"name": "viraj", "image_path": "C:\\Users\\VIRAJ\\Desktop\\miniprojecct\\student_data\\viraj\\viraj.jpg"},
        {"name": "harsh", "image_path": "C:\\Users\\VIRAJ\\Desktop\\miniprojecct\\student_data\\harsh\\harsh.jpg"}
    ]

    known_faces = load_known_faces(attendance_database)
    mark_attendance(attendance_database, student_data, known_faces)
