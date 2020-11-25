# Face Mask detector Using Rgb images

This reposiotry implements a face mask detector. It is able to detect faces of people wearing mask. It automatically discard faces without.
It uses haar cascade custom model trained on a custom dataset.
The dataset is available inside the dataset folder.

## Setup 

1. Setup env

```
virtualenv --python=python3 env
source env/bin/activate
pip install -r requirements.txt
```

2. Run demo (real time webcam demo)

```
python detector.py
```

## Training

```
Open a terminal
cd face-mask-detector-rgb
python check.py # check if label are correct
python create_bg.py
./train_haar.sh
```
