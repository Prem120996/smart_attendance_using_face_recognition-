🎯 Smart Attendance System Using Face Recognition

📝 Overview

The Smart Attendance System leverages face recognition technology to automate attendance tracking. This system eliminates the need for manual attendance marking by identifying individuals using their facial features in real time.

✨ Features

Face Detection & Recognition – Uses OpenCV and deep learning models.

Automated Attendance Marking – Records attendance with timestamps.

Firebase Integration – Stores and retrieves attendance records securely in Firebase.

User Management – Enables student and faculty registration.

Live Camera Feed Support – Processes real-time facial recognition.

Attendance Reports – Generates detailed reports for easy tracking and analysis.

🔧 Technologies Used

Backend: Python (Flask/Django) 

Frontend: HTML, CSS, JavaScript 

Face Recognition: OpenCV, cvzone

Database: Firebase Firestore

Authentication: Firebase Authentication (OAuth/Email-Password)

🚀 Getting Started

📥 Installation

Clone the repository:

git clone https://github.com/Prem120996/smart_attendance_using_face_recognition-
.git

Navigate to the project directory:

cd smart_attendance_using_face_recognition-

Install backend dependencies:

pip install -r requirements.txt  # For Python-based backend


Install frontend dependencies:

cd frontend
npm install

Set up Firebase:

Create a Firebase project at Firebase Console.

Enable Firestore Database and Authentication.

Download the serviceAccountKey.json file and place it in the backend directory.

Configure Firebase settings in .env or firebase-config.js.

Train the model with registered user faces.

Run the backend server:

python main.py  # For Flask

Run the frontend server:

npm start

📌 Usage

Register Users – Add students and faculty members.

Train the System – Capture and store facial data.

Start Face Recognition – Launch the camera feed for real-time identification.

View Attendance Records – Check and export attendance reports from Firebase.

🔮 Future Enhancements

RFID integration for multi-factor authentication.

Cloud-based storage for remote access.

Mobile app support for enhanced usability.

🤝 Contribution

Contributions are welcome! To contribute:

Fork the repository.

Create a new branch: git checkout -b feature-branch

Commit your changes: git commit -m "Add new feature"

Push to the branch: git push origin feature-branch

Open a Pull Request.

🛡️ License

This project is licensed under the MIT License.

