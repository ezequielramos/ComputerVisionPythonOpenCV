from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("colorida.jpg")
azul, verde, vermelho = cv.split(img)

plt.hist(azul.ravel(), 256, [0,256])
plt.figure()
plt.hist(verde.ravel(), 256, [0,256])
plt.figure()
plt.hist(vermelho.ravel(), 256,[0,256])
plt.show()
