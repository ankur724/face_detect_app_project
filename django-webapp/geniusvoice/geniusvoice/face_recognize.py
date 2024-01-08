# pylint:disable=no-member

import os
import numpy as np
import cv2 as cv
from django.shortcuts import render


def train(request):

    return render(request, 'upload.html')


# Your other imports and code here

def imgtrain(request):
    # Your existing code here

    haar_cascade = cv.CascadeClassifier(
        r'C:\face_detect_app\django-webapp\geniusvoice\geniusvoice\haarcascade_frontalface_default.xml')

    people = ['uv']
    # features = np.load('features.npy', allow_pickle=True)
    # labels = np.load('labels.npy')
    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read(
        r'C:\face_detect_app\django-webapp\geniusvoice\geniusvoice\face_trained.yml')

    # img = cv.imread(
    #     r'C:\face_detect_app\facedetection_opencv\test1.jpg')

    # img = cv.imread(
    #     r'C:\face_detect_app\ankur.jpg')
    # NEW CODE IS THISSSSSSSSSSSSSSS.......................CODE STARTTTTTTTTTTTTTTTTTTT............
    # for thisssssssssss............
    # img = cv.imread(
    #     r'C:\face_detect_app\ankur.jpg')
    # ------------>>>>>>>>>>>>>>..

    # Specify the folder where the images are being uploaded
    image_folder = r'C:\face_detect_app\django-webapp\geniusvoice\media\myimage'

    # List all files in the folder
    image_files = os.listdir(image_folder)

    # Sort the list of files by modification time to get the most recently uploaded image
    image_files.sort(key=lambda x: os.path.getmtime(
        os.path.join(image_folder, x)), reverse=True)

    if image_files:
        # Get the most recently uploaded image
        most_recent_image = image_files[0]

        # Construct the full path to the image
        image_path = os.path.join(image_folder, most_recent_image)

        # Read the image using OpenCV
        img = cv.imread(image_path)

        # Now 'img' contains the most recently uploaded image, and you can process it with OpenCV
    else:
        print("No images found in the specified folder.")

    # CODE ENDSSSSSSSSSSSSSSSSSSSSS.....................NEW CODE....................CODE ENDSSSSSSSSSSSSSSSSSSSSS............

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow('Person', gray)

    # Detect the face in the image
  # Get the recognized name based on the labelnames=""

# Detect the face in the image
# new code to write name

    names = ""
    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]

        label, confidence = face_recognizer.predict(faces_roi)
        # print(f'Label = {people[label]} with a confidence of {confidence}')
        names += people[label] + " "

        cv.putText(img, str(people[label]), (20, 20),
                   cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=1)

    # cv.imshow('Detected Face', img)
    # names = "John Doe Jane Smith"
    cv.imshow('Detected Face', img)

    cv.waitKey(0)
    # return names

    # faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
    # recognized_names = []

    # for (x, y, w, h) in faces_rect:
    #     faces_roi = gray[y:y+h, x:x+w]
    #     context = {'names': recognized_names}
    #     label = face_recognizer.predict(faces_roi)

    #     recognized_name = people[label]

    #     recognized_names.append(recognized_name)

    #     label = face_recognizer.predict(faces_roi)
    #     print(f'Label = {people[label]} with a confidence of {confidence}')

    #     recognized_name = context['names'][label]
    #     recognized_names.append(recognized_name)

    #     cv.putText(img, str(people[label]), (20, 20),
    #                cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    #     cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=1)

    # cv.imshow('Detected Face', img)
    # name_str = "  ".join(name)
    # cv.waitKey(0)
    # cv.imshow('Detected Face', img)

    # Corrected indentation for the return statement
    # namei = label[0]
    cv.destroyAllWindows()

    return render(request, "upload.html")
