import os

path = "static/thermal-dataset/background/background-all"
files = os.listdir(path)
with open("bg.txt", "w") as f:
    for name in files:
        # background/name.png
        fname = os.path.join(path, name)
        f.writelines(fname +"\n")


