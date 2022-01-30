# Draw diff geometric shapes
import cv2

img = cv2.imread('lena.jpg', 1)


# draw lines on an image using cv2 'line' function
# line(image, starting_point, ending point, color-bgr, thichness(1-10))
imgg = cv2.line(img, (40,40), (255,150), (255, 0, 0), 5)
imgg = cv2.arrowedLine(img, (134,34), (350,50), (0, 255, 0), 8)


# rectangle(image, starting_point, ending point, color-bgr, thichness(1-10), lineType, shift)
imgg = cv2.rectangle(img, (240,240), (290,290), (0, 255, 0), 8)
imgg = cv2.rectangle(img, (310,240), (360,290), (0, 255, 0), 8)
imgg = cv2.rectangle(img, (20,420), (70,450), (0, 255, 0), -1)  # change thickness to colorfill
imgg = cv2.rectangle(img, (100,380), (200,480), (0, 255, 0), 10)  # change thickness to colorfill


# circle(image, centre, radius, color-bgr, thichness(1-10), lineType, shift)
imgg = cv2.circle(img, (150,430), 50, (255, 0, 0), -1)
imgg = cv2.circle(img, (400,120), 60, (255, 0, 0), 8)


# Text(image, text, starting_point, fontFace, fontSize, color-bgr, thichness(1-10), lineType)
font = cv2.FONT_HERSHEY_SIMPLEX
imgg = cv2.putText(img, 'OpenCV', (250,400), font, 2, (255, 255, 255), 3, cv2.LINE_AA)
imgg = cv2.putText(img, 'SanmiLeeAI', (250,500), font, 1, (255, 78, 100), 3, cv2.LINE_AA)


cv2.imshow("image", imgg)

cv2.waitKey(0)
cv2.destroyAllWindows()
