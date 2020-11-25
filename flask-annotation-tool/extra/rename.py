import os

path = "static/thermal-dataset/background/background-1"
files = os.listdir(path)

for name in files:
  filename = path+ "/" + name
  n = os.path.splitext(name)[0]
  ext = os.path.splitext(name)[1]
  filename_n = path + "/" + n + "-05-07-2020" + ext
  os.rename(filename,filename_n)
