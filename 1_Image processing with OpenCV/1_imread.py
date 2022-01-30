import cv2

img = cv2.imread("lena.jpg")

cv2.imshow("image", img)


k = cv2.waitKey(0) # close display window with any key


if k == 27:
    cv2.destroyAllWindows()

