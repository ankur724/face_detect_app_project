# import cv2 as cv
# import os
# import numpy as np
# p = []
# DIR = r'C:\\Users\\HP\\Desktop\\OpenCV\\Face recognition\\Images'
# for i in os.listdir('C:\\Users\\HP\\Desktop\\OpenCV\\Face recognition\\Images'):
#     p.append(i)
# print(p)

# pylint:disable=no-member
# Read this post : https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/


import os
import cv2 as cv
import numpy as np

people = ['ankur']
DIR = r'C:\face_detect_app\imagecollect'

haar_cascade = cv.CascadeClassifier(
    r'C:\face_detect_app\haarcascade_frontalface_default.xml')

features = []
labels = []


def create_train():

    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)

            if img_array is None:
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()

print('Training done ---------------')
print(labels)
features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
