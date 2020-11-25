import numpy as np
import cv2
import os

# https://hamelot.io/visualization/using-ffmpeg-to-convert-a-set-of-images-into-a-video/
# ffmpeg -r 1 -i res_video/%01d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p all.mp4

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml

#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (384,288))

face_cascade_thermal = cv2.CascadeClassifier('results/cascade.xml')

path="./static/thermal-dataset/images/images-2/"
path="./static/thermal-dataset/background/background-all/"
files = os.listdir(path)
for filename in files:
    tempPath = os.path.join(path, filename)
    
    im_thermal = cv2.imread(tempPath,0)
    
    #faces_thermal = face_cascade_thermal.detectMultiScale(im_thermal, 1.1,5)
    faces_thermal = face_cascade_thermal.detectMultiScale(im_thermal, 1.05,3)

    im_thermal = cv2.cvtColor(im_thermal, cv2.COLOR_GRAY2RGB)
    #cv2.putText(im_thermal, "THERMAL HAAR ",(10,30), cv2.FONT_HERSHEY_COMPLEX,1, (0,255,0),1)

    for (x,y,w,h) in faces_thermal:
        cv2.rectangle(im_thermal,(x,y),(x+w,y+h),(255,0,0),2)

    #im_out = np.concatenate((im_rgb, im_thermal),axis=1)
    #cv2.imwrite("res_video/"+ filename , im_out)
    #out.write(im_out)
    #cv2.imshow('RGB Classifier',im_rgb)
    cv2.imshow("Thermal Classifier", im_thermal)
    cv2.waitKey(0)


