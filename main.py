import cv2
import os
import datetime
import face_recognition
import numpy as np
import pyglet.media
import threading

# Video capture setup (0 for webcam, 1 for external cam)
cap = cv2.VideoCapture(0)
ws, hs = 1280, 720
cap.set(3, ws)
cap.set(4, hs)

# Load the alarm sound
sound = pyglet.media.load("alarm.wav", streaming=False)

# Load registered face encodings and names
known_face_encodings = []
known_face_names = []
registered_faces_dir = "registered_faces"

# Ensure the registered faces directory exists
if not os.path.exists(registered_faces_dir):
    print(f"Directory '{registered_faces_dir}' not found.")
else:
    for filename in os.listdir(registered_faces_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            face_image = face_recognition.load_image_file(os.path.join(registered_faces_dir, filename))
            face_encodings = face_recognition.face_encodings(face_image)

            # Check if a face encoding is found
            if len(face_encodings) > 0:
                known_face_encodings.append(face_encodings[0])
                known_face_names.append(os.path.splitext(filename)[0])
            else:
                print(f"No face found in {filename}")

# Function to play the alarm in a separate thread
def play_alarm():
    sound.play()

while True:
    success, img = cap.read()
    if not success:
        continue

    # Detect faces in the current frame
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_img)
    face_encodings = face_recognition.face_encodings(rgb_img, face_locations)

    # Check each detected face
    for (face_encoding, face_location) in zip(face_encodings, face_locations):
        # Compare with registered faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # If the face is unknown, trigger the alarm and save the image
        if name == "Unknown":
            # Play alarm sound in a thread
            sound_thread = threading.Thread(target=play_alarm)
            sound_thread.start()

            # Save the detected unknown face
            now = datetime.datetime.now()
            date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
            directory = 'Detected_Unknown_Faces'
            if not os.path.exists(directory):
                os.makedirs(directory)
            cv2.imwrite(f"{directory}/{date_time}.jpg", img)
            print(f"Unknown face detected and saved as {date_time}.jpg")

    # Display the frame
    cv2.imshow("Press ESC To Exit", img)

    # Exit when the ESC key is pressed
    if cv2.waitKey(1) == 27:
        break

# Release video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
