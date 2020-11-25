import numpy as np
import cv2
import os

#SIZE = (382,288)

filename = "training.txt"
c  =0 
#filename_new = "info_nn.txt"
with open(filename) as f:
    lines = [line.rstrip() for line in f]
    for line in lines:
        line_list = line.split(" ")
        path = line_list[0]
        name = path.split("/")[-1]


        '''
        if "-05-07-2020" in path:
            x = int(line_list[2])
            y = int(line_list[3])
            w = int(line_list[4])
            h = int(line_list[5])
            f=open(filename_new,"a+")
            f.write(path + " " + str(1) + " " + str(x) + " " + str(y) + " " + str(w-x) + " " + str(h-y) + "\n")
            f.close()
        else:
            f=open(filename_new,"a+")
            f.write(line + "\n") 
            f.close()
        '''
        
        #print(path)
        x = int(line_list[2])
        y = int(line_list[3])
        w = int(line_list[4])
        h = int(line_list[5])
        #print(x,y,w,h)

        imin = cv2.imread(path,0)
        im = cv2.imread(path,0)
        #im = cv2.resize(im,SIZE)
        cv2.circle(im, (x,y), 10, (0,255,0))
        #img = im[y:(y+h),x:(x+w)]
        #im = cv2.equalizeHist(im)
        #cv2.imwrite("glass/"+ str(c) + ".png", img )
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        
        #nn = "images/test/"+name
        #cv2.imwrite(nn, im)
            
        c=c+1
        cv2.imshow("img", im)
        cv2.waitKey(0)