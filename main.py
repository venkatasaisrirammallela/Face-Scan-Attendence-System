import streamlit as st
import cv2
import face_recognition
import pickle
import numpy as np
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
import io
from PIL import Image

# Initialize Firebase Admin


# Load the known face encodings and IDs
with open('EncodeFile.p', 'rb') as file:
    encodeListKnownWithIds = pickle.load(file)
    encodeListKnown, studentIds = encodeListKnownWithIds

# Function to mark attendance
def mark_attendance(studentId):
    ref = db.reference(f'/Students/{studentId}')
    student_data = ref.get()
    
    if student_data is not None:
        last_attendance_time = student_data.get('last_attendance_time')
        
        # Check if the attendance was already marked for today
        today_date = datetime.now().strftime('%Y-%m-%d')
        if last_attendance_time is None or last_attendance_time.split(' ')[0] != today_date:
            ref.update({
                'last_attendance_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            return True  # Attendance was successfully marked
    return False  # Attendance was already marked or no student data found

# Streamlit app
st.title("Face Attendance System")

if st.button("Start Attendance"):
    st.write("Capturing image...")

    # Capture a single image from the webcam
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    video_capture.release()

    if ret:
        # Convert the frame to PIL Image
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(image)
        
        # Process the captured image
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        attendance_marked = False
        recognized_student_id = None

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(encodeListKnown, face_encoding)
            face_distances = face_recognition.face_distance(encodeListKnown, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                studentId = studentIds[best_match_index]
                attendance_marked = mark_attendance(studentId)
                recognized_student_id = studentId

                # Draw a box around the face and label it with the student's ID
                top, right, bottom, left = [v * 4 for v in face_location]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, studentId, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

                break

        # Convert the frame with annotations to PIL Image
        annotated_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
        # Show the image and status
        st.image(annotated_image, caption='Captured Image', use_column_width=True)

        if attendance_marked:
            st.success(f"Attendance marked for Student ID: {recognized_student_id}")
        elif recognized_student_id:
            st.warning(f"Attendance already marked for Student ID: {recognized_student_id}")
        else:
            st.warning("No face detected or face not recognized.")
    else:
        st.error("Failed to capture image.")
