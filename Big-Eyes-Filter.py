# open camera and add a filter to the eyes (Big Eyes)

import cv2 as cv
import numpy as np


face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap = cv.VideoCapture(0)

#Check if the webcam is opened correctly
if not cap.isOpened():
     raise IOError("Cannot open webcam")

scale = 10
while True:
    ret, frame = cap.read()
    frame = cv.flip(frame,1)

    face = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x, y, w, h) in face :
        cv.rectangle(frame, (x,y), (x+w , y+h), (0, 255, 0), 3)
        face_pos = frame[x:x+w , y:y+h]

    eyes = eye_cascade.detectMultiScale(frame)    
    for (ex, ey, ew, eh) in eyes:
        #  cv.rectangle(frame, (ex,ey), (ex+ew , ey+eh), (255, 0, 0), 3)
         eyes_pos = frame[ey:ey+eh, ex:ex+ew, :]
         eyes_zoom = cv.resize(eyes_pos, None, fx=1.3, fy=1.3, interpolation=cv.INTER_CUBIC)
         dimensions = eyes_zoom.shape
         frame[ey-5:ey-5+dimensions[0],ex-5:ex-5+dimensions[1],:] = eyes_zoom


    # added_image = cv.addWeighted(frame, 0.5, eyes_pos, 0.5, 0)    
    cv.imshow('Camera', frame)

    c = cv.waitKey(1)
    if c == 27:     # Exit on Escape
        break


cap.release()
cv.destroyAllWindows()
print(dimentsions)
print(ew, eh)
