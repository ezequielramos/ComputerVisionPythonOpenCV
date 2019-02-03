from cv2 import cv2 as cv

img = cv.imread("head.PNG")
imgBlur = cv.blur(img, (5,5))
imgGaussian = cv.GaussianBlur(img, (5,5), 0)
imgMedian = cv.medianBlur(img, 5)

cv.imshow('img', img)
cv.imshow('img blur',imgBlur) #substitui cada pixel pela valor medio de sua vizinhanca
cv.imshow('img gaussian',imgGaussian) #excelente resulltado para tratamento de ruidos gaussiano
cv.imshow('img median',imgMedian) #excelente resultado para tratamento de ruidos sal e pimenta

cv.waitKey(0)
cv.destroyAllWindows()