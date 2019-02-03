from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('cafe.jpg', 0)

metodo = cv.THRESH_BINARY_INV + cv.THRESH_OTSU 

ret, imgBin = cv.threshold(img, 0, 255, metodo) # pixels com valores entre o limiar sao considerado como objeto de interesse

plt.hist(img.ravel(), 256, [0,256])

cv.imshow('original', img)
cv.imshow('imgBin', imgBin)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()