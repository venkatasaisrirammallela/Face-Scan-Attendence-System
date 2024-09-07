import cv2
import face_recognition
import os
import pickle
import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase Admin
cred = credentials.Certificate(r"C:\Users\venka\Downloads\firebasepath.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancesystem-38a01-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancesystem-38a01.appspot.com"  # Use the bucket name without 'gs://'
})

folderPath = r'C:\Users\venka\OneDrive\Desktop\attendence\Images'
PathList = os.listdir(folderPath)
imgList = []
studentIds = []

for path in PathList:
    try:
        # Full path to the image
        fileName = os.path.join(folderPath, path)
        
        # Read the image from the folder
        img = cv2.imread(fileName)
        if img is not None:
            imgList.append(img)
            print(f"Image loaded: {fileName}")

            # Extract the student ID (without the file extension)
            studentId = os.path.splitext(path)[0]
            studentIds.append(studentId)

            # Upload the image to Firebase Storage
            try:
                bucket = storage.bucket()  # Get the default storage bucket
                blob = bucket.blob(f'Images/{path}')  # Create a blob in the Images directory in the bucket
                print(f"Uploading {fileName} to {blob.name}...")
                blob.upload_from_filename(fileName)  # Upload the image file
                print(f"Successfully uploaded {path} to Firebase Storage.")
            except Exception as upload_error:
                print(f"Error uploading {path}: {upload_error}")
        else:
            print(f"Warning: Could not read image {path}. Skipping this file.")
    except Exception as e:
        print(f"Error processing {path}: {e}")

print("Student IDs:", studentIds)


def findEncodeings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

print("Encoding Started....")
encodeListKnown = findEncodeings(imgList)
encodeListKnownWithIds = [encodeListKnown,studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds,file)
file.close
print("File Saved")