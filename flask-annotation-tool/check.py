import numpy as np
import cv2
import os

filename = "res.txt"
c  =0 
#filename_new = "info_nn.txt"
with open(filename) as f:
    lines = [line.rstrip() for line in f]
    for line in lines:
        line_list = line.split(" ")
        path = line_list[0]


        x = int(line_list[2])
        y = int(line_list[3])
        w = int(line_list[4])
        h = int(line_list[5])
        #print(leftx,lefty,bottomx,bottomy)
        im = cv2.imread(path,1)
        img = im[y:(y+h),x:(x+w)]
        #im = cv2.equalizeHist(im)
        #cv2.imwrite("glass/"+ str(c) + ".png", img )
        #cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        c=c+1
        cv2.imshow("im", im)
        cv2.imshow("img", img)
        
        cv2.waitKey(0)
        