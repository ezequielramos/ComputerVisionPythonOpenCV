from cv2 import cv2 as cv
import numpy as np

img = cv.imread('cafe.jpg', 0)
img2 = cv.imread('olho.PNG', 0)

metodo = cv.THRESH_BINARY_INV # objeto de interesse na cor branca
#metodo = cv.THRESH_BINARY # objeto de interesse na cor preta

ret, imgBin = cv.threshold(img, 200, 255, metodo) # pixels com valores entre o limiar sao considerado como objeto de interesse

img_gaussian = cv.medianBlur(img2, 7)

#diferentes valores de limiar para cada regiao da imagem
#obtem melhor resultado considerando constraste
mean = cv.adaptiveThreshold(img_gaussian, 255, cv.ADAPTIVE_THRESH_MEAN_C, metodo, 11, 5) 
gaussian = cv.adaptiveThreshold(img_gaussian, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, metodo, 11, 2)

cv.imshow('original', img)
cv.imshow('imgBin', imgBin)
cv.imshow('mean', mean)
cv.imshow('gaussian', gaussian)

cv.waitKey(0)
cv.destroyAllWindows()