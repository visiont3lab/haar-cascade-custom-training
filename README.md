# Machine learning applied to object detection

## 1. Get a dataset: Scraping using Selenium

* We are going to use selenium library to retrieve google images associated to a specific query.
* Another interesting tool for collecting dataset is [**Google Dataset Search**](https://datasetsearch.research.google.com/)
* Label data using [**Online Labeling Tool (MakeSense)**](https://www.makesense.ai/)

```
# Setup selenium colab: https://stackoverflow.com/questions/51046454/how-can-we-use-selenium-webdriver-in-colab-research-google-com
!pip install selenium
!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
```
## 2. Install opencv

```
sudo apt install opencv
```

Useful References:

* **PyImageSearch** [Image Pyramid](https://www.pyimagesearch.com/2015/03/16/image-pyramids-with-python-and-opencv/)
* **PyImageSearch** [Sliding window](https://www.pyimagesearch.com/2015/03/23/sliding-windows-for-object-detection-with-python-and-opencv/)
* **PyImageSearch** [Python library imutils](https://github.com/jrosebr1/imutils)
* [Online Labeling Tool (MakeSense)](https://www.makesense.ai/)
* [Training haar cascade](https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html)