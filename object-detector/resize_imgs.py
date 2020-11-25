import os
import cv2

def resize_folder_images(inp_folder,out_folder):
    try:
        os.mkdir(out_folder)
    except OSError:
        print ("Creation of the directory %s failed" % out_folder)

    names = os.listdir(inp_folder)
    for name in names:
        fn = os.path.join(inp_folder,name)
        im = cv2.imread(fn,1)

        #https://stackoverflow.com/questions/44650888/resize-an-image-without-distortion-opencv
        width=512
        (h, w) = im.shape[:2]
        r = width / float(w)
        dim = (width, int(h * r))

        im =cv2.resize(im, dim)
        fw = os.path.join(out_folder,name.replace(" ","_"))
        cv2.imwrite(fw,im)

# resize mask images
resize_folder_images(inp_folder="dataset/mask", out_folder="dataset/mask-resize")

# resize without mask images
resize_folder_images(inp_folder="dataset/no-mask", out_folder="dataset/no-mask-resize")
