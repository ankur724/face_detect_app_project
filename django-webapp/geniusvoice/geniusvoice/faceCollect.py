import cv2
import os
import numpy as np
# CODE FOR EXCEUTING PYTHON FILES
from django.shortcuts import render


def button(request):

    return render(request, 'collect.html')


def output(request):

    output_data = "Your Photo sample is being collected successfully ."

    def face_extractor(img):
        # Function detects faces and returns the cropped face
        # If no face detected, it returns the input image
        face_classifier = cv2.CascadeClassifier(
            r'C:\face_detect_app\django-webapp\geniusvoice\geniusvoice\face_dectect.xml')
        # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(img, 1.3, 5)

        if faces is ():
            return None

        # Crop all faces found
        for (x, y, w, h) in faces:
            x = x-10
            y = y-10
            cropped_face = img[y:y+h+50, x:x+w+50]

        return cropped_face

    # Initialize Webcam
    cap = cv2.VideoCapture(0)
    count = 0

    # Collect 100 samples of your face from webcam input
    while True:

        ret, frame = cap.read()
        if face_extractor(frame) is not None:
            count += 1
            face = cv2.resize(face_extractor(frame), (400, 400))
            # face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # Save file in specified directory with unique name

            # file_name_path = os.path.join(
            #     'PhotosCollect', str(count) + '.jpg')
            # output_dir = os.path.join(
            #     'PhotosCollect')

            # if not os.path.exists(output_dir):
            #     os.makedirs(output_dir)

            # # cv2.imwrite({file_name_path}, face)
            # cv2.imwrite(file_name_path, face)


# Get the user's username, replace 'user_username' with your method of obtaining the username

            # Get the user's username, replace 'user_username' with your method of obtaining the username
            # Change this based on how you get the username
            user_username = request.user.username

            # Define the base directory where user folders will be created
            base_dir = os.path.join('PhotosCollect', user_username)

            # Check if the user's folder exists, and create it if not
            if not os.path.exists(base_dir):
                os.makedirs(base_dir)

            # List existing image files in the user's folder
            existing_images = os.listdir(base_dir)

            # Check the number of existing images
            num_existing_images = len(existing_images)

            # Define the maximum number of images to collect per user (e.g., 50)
            max_images_per_user = 50

            if num_existing_images < max_images_per_user:
                # Generate a filename using an incremental counter
                image_number = num_existing_images + 1
                file_name = f"{user_username}_{image_number}.jpg"

                # Set the full file path for the image
                file_path = os.path.join(base_dir, file_name)

                # Save the image
                cv2.imwrite(file_path, face)
            else:
                # Handle the case where the user has already collected the maximum number of images
                print("Maximum number of images collected for this user.")

            # Put count on images and display live count
            cv2.putText(face, str(count), (50, 50),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', face)

        else:
            print("Face not found")
            pass
        if cv2.waitKey(10) == 13 or count == 50:  # 13 is the Enter Key
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Collecting Samples Complete")
    return render(request, "collect.html", {"output_data": output_data})
