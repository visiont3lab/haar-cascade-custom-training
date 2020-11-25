#!/bin/bash

# Info
# https://answers.opencv.org/question/4368/traincascade-error-bad-argument-can-not-get-new-positive-sample-the-most-possible-reason-is-insufficient-count-of-samples-in-given-vec-file/
# https://docs.opencv.org/master/dc/d88/tutorial_traincascade.html
# https://dbloisi.github.io/tutorial/balldetection.html
# To speed up training recompile opencv multitrheading (TBB ON)
# Remove installed opencv sudo rm /usr/local/{bin,lib}/*opencv* 
# https://answers.opencv.org/question/10/how-to-build-opencv-with-tbb-support/
# cd /home/manuel/thermohuman_ws/lib/opencv-3.4.0/release && cmake -D CMAKE_BUILD_TYPE=RELEASE -D WITH_CUDA=OF -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D BUILD_PYTHON_SUPPORT=ON  ..

# Set input
results="cascade_training/results-large"
images_folder="dataset/large/mask-resize"
images_txt="training_large.txt"                  #337
backgrounds_txt="background_large.txt" #1109
num_images=600 #441  # 4863 not ok
num_pos=400   #400 # 500 # almost 90% to select this number https://answers.opencv.org/question/24241/my-classifier-using-haar-cascade-can-not-detect-anything/
num_neg=800 # 250

# remove results and trainining txt files
if [ -d $results ]; then rm -Rf $results; fi
if [ -f positive.vec ]; then rm -f positive.vec; fi

# create resutl folder
mkdir -p $results

# Create positive.vec
# opencv_traincascade -data results -vec positive.vec -bg bg.txt -numPos 500 -numNeg 250 -numStages 10 -w 24 -h 24 
opencv_createsamples -info $images_txt -vec positive.vec -num $num_images   -w 24 -h 24


# Train
#opencv_traincascade -data $results -vec positive.vec -bg $backgrounds_txt -numPos $num_pos -numNeg $num_neg # default: -minHitRate 0.995  -maxFalseAlarmRate 0.5 
opencv_traincascade -data $results -vec positive.vec -bg $backgrounds_txt -numStages 20 -numPos $num_pos -numNeg  $num_neg  -minHitRate 0.995  -maxFalseAlarmRate 0.5 -w 24 -h 24 # -mode ALL  #-precalcValBufSize 4096 -precalcIdxBufSize 4096
