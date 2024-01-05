# Face Recognition for Attendance Tracking

This project aims to create a face recognition system that can evaluate the daily attendance of students in a class. The system consists of a web interface and a machine learning algorithm that can detect and identify faces in images.

## Overview

The system allows users (teachers and higher officials) to upload images of a class and get the names of the students who were present in the photo. The system also provides an option to download the attendance data in an excel sheet. The system uses authentication to prevent students from uploading photos by themselves to avoid proxies.

## Technical Stacks

The system uses the following technical stacks:

- *face_recognition*: A Python library that provides face detection and recognition capabilities¹.
- *sq-lite*: A lightweight relational database management system that stores the face data and attendance records².
- *scikit-learn*: A Python library that provides machine learning tools and models³.
- *django*: A Python web framework that handles the web interface and the backend logic⁴.
- *pandas*: A Python library that provides data analysis and manipulation tools⁵.

## Installation and Usage

To install and run the system, follow these steps:

1. Clone the project repository from GitHub.
2. Install the required dependencies using pip install -r requirements.txt.
3. Run python manage.py migrate to create the database tables.
4. Run python manage.py createsuperuser to create an admin user.
5. Run python manage.py runserver to start the web server.
6. Open http://localhost:8000/ in a browser and log in with the admin credentials.
7. Use the web interface to upload images, view attendance, and download excel sheets.

## Training and Testing

To train and test the face recognition model, follow these steps:

1. Create a folder named training inside the project directory and put the images of the students in subfolders named after their names. For example, training/Alice/alice1.jpg, training/Bob/bob1.jpg, etc.
2. Run python train.py to train the model and save it as model.pkl.
3. Create a folder named testing inside the project directory and put the images of the classes in it. For example, testing/class1.jpg, testing/class2.jpg, etc.
4. Run python test.py to test the model and print the results.

## References

¹: [face_recognition](https://github.com/ageitgey/face_recognition)
²: [SQLite](https://www.sqlite.org/index.html)
³: [scikit-learn](https://scikit-learn.org/stable/)
⁴: [Django](https://www.djangoproject.com/)
⁵: [pandas](https://pandas.pydata.org/)
: [GitHub repository](https://github.com/your_username/your_project_name)

Source: 9/11/2023
(1) Build Your Own Face Recognition Tool With Python. https://realpython.com/face-recognition-with-python/.
(2) Creating a Face Database for Edge AI Facial Recognition. https://www.codeproject.com/Articles/5306645/Creating-a-Face-Database-for-Edge-AI-Facial-Recogn.
(3) (DOC) Face recognition Project | Kent Steven - Academia.edu. https://www.academia.edu/21802319/Face_recognition_Project.
(4) A PROJECT REPORT ON FACE RECOGNITION SYSTEM WITH FACE DETECTION. https://www.academia.edu/38912204/A_PROJECT_REPORT_ON_FACE_RECOGNITION_SYSTEM_WITH_FACE_DETECTION.
(5) Face Detection Project in Python [In 5 Easy Steps] - upGrad. https://www.upgrad.com/blog/face-detection-project-in-python/.
