from cv2 import cv2 as cv

img = cv.imread("cafe.jpg", 0)
imgGaussian = cv.GaussianBlur(img, (5,5), 0)

metodo = cv.THRESH_BINARY_INV # objeto de interesse na cor branca

ret, imgBin = cv.threshold(imgGaussian, 100, 255, metodo) # pixels com valores entre o limiar sao considerado como objeto de interesse
imgSeg = cv.Canny(imgBin, 100, 200)

cv.imshow('img', imgGaussian)
cv.imshow('img bin',imgBin) #excelente resulltado para tratamento de ruidos gaussiano
cv.imshow('img gaussian',imgSeg)

cv.waitKey(0)
cv.destroyAllWindows()