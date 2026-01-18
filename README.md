# Face Recognition Attendance System

A simple **Face Recognition-based Attendance System** built using Python, Flask, and OpenCV. This project captures faces through a webcam, matches them with pre-stored images, and records attendance automatically in a CSV file.

## Features
- Real-time face detection using webcam
- Matches faces with known images stored in the system
- Automatically records attendance with timestamp in a CSV file
- Easy to add new users by uploading their images

## Technologies Used
- **Python** – Backend logic and face recognition
- **Flask** – Web interface for capturing images
- **OpenCV** – Image and video processing
- **face_recognition** – Face encoding and matching
- **HTML/CSS/JavaScript** – Frontend for webcam interface
- **CSV** – Attendance storage

## Project Structure
Face-Recognition-Attendance/
├── app.py # Flask backend
├── templates/
│ └── index.html # Frontend
├── static/
│ ├── images/ # Known face images
│ └── captured/ # Captured attendance images
├── Attendance.csv # Output attendance file
└── README.md

bash
Copy code

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/YourUsername/Face-Recognition-Attendance.git
cd Face-Recognition-Attendance
Install dependencies:

bash
Copy code
pip install flask opencv-python face_recognition numpy
Add known images to static/images/.

Run the Flask app:

bash
Copy code
python app.py
Open http://127.0.0.1:5000/ in your browser to access the webcam interface.

Usage
Click Start to activate webcam

Click Capture & Submit to record attendance

Attendance is saved in Attendance.csv with timestamps

Sample Attendance Output
less
Copy code
PRABHAKARAN D,18:23:48
AI KING,18:26:25
PRAVEENRAJA S,18:26:46
KARTHIKEYAN P,18:29:59
SARAN,18:32:47
MASTER,18:33:14
SIVABALAN S,15:57:03
PRAVEENRAJA S,15:57:20
SRI DHARANIVEL A M,15:57:42
ASWIN SANJEEV KUMAR A,16:02:29
Future Improvements
Support multiple faces in one frame

Integrate with a database instead of CSV

Email notifications for absent students

Improved UI/UX for better user experience