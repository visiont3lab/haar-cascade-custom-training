import numpy as np
import cv2
import os

filename = "res.txt"
with open(filename) as f:
    lines = [line.rstrip() for line in f]
    for line in lines:
        line_list = line.split(" ")
        path = line_list[0]
        name = path.split("/")[-1]

        filenamepath = "./static/images/to_label/"+name
        print(filenamepath)
        im = cv2.imread(filenamepath,0)
        cv2.imwrite("imfin/"+name, im)
        
        