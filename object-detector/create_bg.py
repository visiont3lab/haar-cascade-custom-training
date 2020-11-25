import os

path = "dataset/no-mask-resize"
files = os.listdir(path)
with open("background.txt", "w") as f:
    for name in files:
        # background/name.png
        fname = os.path.join(path, name)
        f.writelines(fname +"\n")


