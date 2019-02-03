from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("Cinza.jpg")

plt.hist(img.ravel(), 256, [0,256])
plt.show()

