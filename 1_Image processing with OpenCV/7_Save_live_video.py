# Save input video
import cv2

cap = cv2.VideoCapture(0)

# describe 4cc format
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# output video parameter: output name, 4cc format, 20frames/sec, (width, height)
out = cv2.VideoWriter('ouput1.avi', fourcc, 20.0, (640, 480))


while (True):
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow("image_frame", frame)
        out.write(frame)

        if cv2.waitKey(1) == ord('q'):
            break

    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()
