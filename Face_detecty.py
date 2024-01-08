import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions =(width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('photos\profile image.jpeg')
# rescaleFrame(img,scale = 0.50)
# img = cv.resize(img,(1680,1050))
print(img.shape)
# cv.imshow('LovelyKristin', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray People', gray)

# haar_cascade = cv.CascadeClassifier('C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
haar_cascade = cv.CascadeClassifier('C:\Users\HP\AppData\Local\Programs\Python\Python310\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)



cv.waitKey(0)