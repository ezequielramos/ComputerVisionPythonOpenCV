from cv2 import cv2 as cv
import numpy as np

img = cv.imread('moeda.PNG', 0)
img2 = cv.imread('raiox.jpg', 0)

elem_str1 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
elem_str2 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (21,21))

imgProc = cv.morphologyEx(img, cv.MORPH_GRADIENT, elem_str1)
imgProc2 = cv.morphologyEx(img2, cv.MORPH_TOPHAT, elem_str2)
imgProc3 = cv.morphologyEx(img2, cv.MORPH_BLACKHAT, elem_str2)

cv.imshow('img', imgProc)
cv.imshow('img_process', imgProc2)
cv.imshow('img_process_dilate', imgProc3)

cv.waitKey(0)
cv.destroyAllWindows()