from cv2 import cv2 as cv
import numpy as np

img = cv.imread("placa.PNG")

element_estr = cv.getStructuringElement(cv.MORPH_RECT, (7,7))
element_estr_cross = cv.getStructuringElement(cv.MORPH_CROSS, (7,7))

img_process = cv.erode(img, element_estr, iterations = 2)
img_process_dilate = cv.dilate(img, element_estr_cross, iterations = 2)
cv.imshow('img', img)
cv.imshow('img_process', img_process)
cv.imshow('img_process_dilate', img_process_dilate)

cv.waitKey(0)
cv.destroyAllWindows()