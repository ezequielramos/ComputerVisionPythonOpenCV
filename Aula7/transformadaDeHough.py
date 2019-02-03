from cv2 import cv2 as cv
import numpy as np

img = cv.imread("estrada.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgGaussian = cv.GaussianBlur(gray, (5,5), 0)

metodo = cv.THRESH_BINARY_INV # objeto de interesse na cor branca

ret, imgBin = cv.threshold(imgGaussian, 100, 255, metodo) # pixels com valores entre o limiar sao considerado como objeto de interesse
imgSeg = cv.Canny(imgBin, 100, 200)

#cv.HoughLines() # mais pesada porque considera todos pixels da imagem
lines = cv.HoughLinesP(imgSeg, 1, np.pi/180, 10, 200) # mais leve porque considera um grupo de pixels aleatorios da imagem

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0,255,0), 3)

cv.imshow('img', imgGaussian)
cv.imshow('img bin',imgBin) #excelente resulltado para tratamento de ruidos gaussiano
cv.imshow('img gaussian',imgSeg)
cv.imshow('img aa',img)

cv.waitKey(0)
cv.destroyAllWindows()