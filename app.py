Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from flask import Flask, render_template, Response
import cv2
import face_recognition
import pickle
import numpy as np
import firebase_admin
from firebase_admin import credentials, db, storage
from datetime import datetime

app = Flask(__name__)

# Firebase setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "",
    'storageBucket': ""
})
bucket = storage.bucket()

# Load the encoding file
with open('EncodeFile.p', 'rb') as file:
    encodeListKnownWithIds = pickle.load(file)
encodeListKnown, studentIds = encodeListKnownWithIds

# Video capture setup
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

@app.route('/')
def index():
...     return render_template('index.html')
... 
... def generate_frames():
...     while True:
...         success, img = cap.read()
...         if not success:
...             break
...         else:
...             imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
...             imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
... 
...             faceCurFrame = face_recognition.face_locations(imgS)
...             encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
... 
...             if faceCurFrame:
...                 for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
...                     matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
...                     faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
...                     matchIndex = np.argmin(faceDis)
... 
...                     if matches[matchIndex]:
...                         id = studentIds[matchIndex]
...                         studentInfo = db.reference(f'Students/{id}').get()
...                         # Update attendance and other logic here
... 
...             ret, buffer = cv2.imencode('.jpg', img)
...             frame = buffer.tobytes()
... 
...             yield (b'--frame\r\n'
...                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
... 
... @app.route('/video_feed')
... def video_feed():
...     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
... 
... if __name__ == "__main__":
