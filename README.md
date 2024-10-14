# DON'T IGNORE!!


Make 2 folders

1. Register_faces

2. Detected Unknown Faces


# face_authentication

Project Overview

This project uses machine learning to create a face recognition system that compares detected faces against pre-uploaded images. If an unregistered face is detected, the system captures an image of the face with a timestamp and plays a notification sound using a .wav file.


Components Used:

Python (OpenCV, NumPy, etc.)

Machine Learning Libraries (Face recognition models)

Camera/Webcam

Folder for Registered Faces (register face folder)

Audio File for Notification (alert.wav)


How It Works:

Face Registration: Initially, users can upload face images to the 'register face' folder. These images act as a reference for future face detections.

Face Detection: The system continuously monitors the input from the camera, detecting faces in real-time.

Face Recognition: Each detected face is compared against the registered faces in the folder.

If the detected face matches an uploaded face, no action is taken.

If the detected face is not recognized, the system captures an image with the date and time stamped, stores it, and plays a notification sound using a .wav file.

Notification and Logging: The system ensures any unregistered face is promptly logged with a visual record and an audio alert.


Key Features:

Real-time face detection and recognition using machine learning.

Automatically captures images of unrecognized faces with a timestamp.

Plays a .wav notification file when an unknown face is detected.

Simple face registration process by adding images to a folder.

Efficient face matching using machine learning algorithms.


Applications:

Home security systems for monitoring visitors or intruders.

Office access control where only registered employees are allowed.

Attendance systems that log unrecognized faces.


Instructions:

Upload face images into the 'register face' folder.

Ensure the camera/webcam is connected and functioning.

Run the provided Python script to start monitoring.

If an unregistered face is detected, the system will save an image with the date and time, and play a notification sound.

