# Read image height and width
import cv2

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    cv2.imshow("image_frame", frame)

    wid = cap.get(cv2.CAP_PROP_FRAME_WIDTH)    # 640
    hght = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)   # 480

    print(wid, ":", hght)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
