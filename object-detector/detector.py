import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier('cascade_training/results/cascade.xml')

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, im_color = cap.read()


    # Our operations on the frame come here
    im_gray = cv2.cvtColor(im_color, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(im_gray, 1.1,5)

    for (x,y,w,h) in faces:
        roi = im_gray[y:y+h,x:x+w]
        cv2.rectangle(im_color,(x,y),(x+w,y+h),(255,0,0),2)


    # Display the resulting frame
    cv2.imshow('frame',im_color)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

