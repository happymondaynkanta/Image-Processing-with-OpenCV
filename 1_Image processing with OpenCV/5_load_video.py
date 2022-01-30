# display image from file
import cv2

# load video from disk
cap = cv2.VideoCapture('vtest.avi')

while (True):
  ret, frame = cap.read()
  cv2.imshow("image_frame", frame)

  if cv2.waitKey(1) == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()
