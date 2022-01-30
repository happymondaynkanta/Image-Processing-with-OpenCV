# set video_frame properties
import cv2

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 640
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   # 480

# recall that ""cv2.CAP_PROP_FRAME_WIDTH == 3"" & ""cv2.CAP_PROP_FRAME_HEIGHT == 4""
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)    # 640
cap.set(4, 720)   # 480

print(cap.get(3))   # 1280
print(cap.get(4))   # 720

while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow("image_frame", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
