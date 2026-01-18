import os
from flask import Flask, render_template, request, jsonify
import face_recognition
import cv2
import numpy as np
from datetime import datetime

# Setup
KNOWN_DIR = 'static/images'
CAPTURE_DIR = 'static/captured'
CSV_FILE = 'Attendance.csv'

os.makedirs(KNOWN_DIR, exist_ok=True)
os.makedirs(CAPTURE_DIR, exist_ok=True)

app = Flask(__name__)

# Load known faces
known_encodings = []
known_names = []

for file in os.listdir(KNOWN_DIR):
    path = os.path.join(KNOWN_DIR, file)
    image = cv2.imread(path)
    if image is None:
        print(f"Warning: {file} could not be loaded.")
        continue
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb)
    if encodings:
        known_encodings.append(encodings[0])
        known_names.append(os.path.splitext(file)[0])
    else:
        print(f"No face found in {file}")

# Record attendance
def record_attendance(name):
    try:
        # Open file in append mode, create it if it doesn't exist
        with open(CSV_FILE, 'a', newline='') as file:
            now = datetime.now().strftime('%H:%M:%S')
            file.write(f'{name},{now}\n')
            print(f"{name} recorded at {now}")
    except Exception as e:
        print(f"Error recording attendance: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')  # Make sure this is the correct file name

@app.route('/upload', methods=['POST'])
def upload():
    try:
        print("Upload route hit")

        file = request.files.get('image')
        if not file:
            print("No file received")
            return jsonify({'status': 'No file received'})

        image_path = os.path.join(CAPTURE_DIR, 'captured_image.jpg')
        file.save(image_path)
        print("File saved to", image_path)

        image = cv2.imread(image_path)
        if image is None:
            print("cv2.imread failed")
            return jsonify({'status': 'Failed to read image'})

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(rgb_image)

        if not face_encodings:
            print("No face detected")
            return jsonify({'status': 'No face detected'})

        face_encoding = face_encodings[0]
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if face_distances[best_match_index] < 0.6:
            name = known_names[best_match_index]
            record_attendance(name)  # Directly add to CSV
            print("Match found:", name)
            return jsonify({'status': 'Face matched', 'name': name})
        else:
            print("No match found")
            return jsonify({'status': 'Person not found'})

    except Exception as e:
        print("Exception:", str(e))
        return jsonify({'status': 'Server error: ' + str(e)})

if __name__ == '__main__':
    app.run(debug=True)
