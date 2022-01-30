# imread, imshow, imwrite
import cv2

img1 = cv2.imread('lena.jpg', 1)	# color image
img2 = cv2.imread('lena.jpg', 0)	# gray image
img3 = cv2.imread('lena.jpg', -1)	# default image


cv2.imshow('image', img1)
cv2.waitKey(2000)  # close display window after 2 secs


cv2.imshow('image', img2)
cv2.waitKey(2000)


cv2.imshow('image', img3)
cv2.waitKey(2000)


cv2.destroyAllWindows()
