# using the if ret = true function
import cv2
import datetime

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Width: " + str(cap.get(3)) + " & Height: " + str(cap.get(4))
        timey = str(datetime.datetime.now())

        frame = cv2.putText(frame, text, (10,40), font, 1, (0, 255, 255), 1, cv2.LINE_AA)
        frame = cv2.putText(frame, timey, (10,90), font, 1, (255, 0, 0), 1, cv2.LINE_AA)
        frame = cv2.putText(frame, 'OpenCV', (10,150), font, 1, (255, 255, 255), 1, cv2.LINE_AA)


        cv2.imshow('image_frame', frame)


        if cv2.waitKey(1) == ord('q'):
            break

    else:
        break



cap.release()
cv2.destroyAllWindows()
