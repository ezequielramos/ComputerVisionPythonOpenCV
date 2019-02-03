from cv2 import cv2 as cv

img = cv.imread("predio.JPG", 0)

sobelx = cv.Sobel(img, cv.CV_8U, 1, 0, ksize=7)
sobely = cv.Sobel(img, cv.CV_8U, 0, 1, ksize=7)
laplacian = cv.Laplacian(img, cv.CV_8U)

cv.imshow("sobelx", sobelx)
cv.imshow("sobely", sobely)
cv.imshow("laplacian", laplacian)

cv.waitKey(0)
cv.destroyAllWindows()