import cv2
import numpy as np

video = cv2.VideoCapture(0)
background = np.zeros((480, 640, 3), dtype=np.uint8)

while True:
    ret, frame = video.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    lower_black = np.array([30, 30, 0])
    upper_black = np.array([104, 153, 70])
    mask = cv2.inRange(frame, lower_black, upper_black)

    foreground = cv2.bitwise_and(frame, frame, mask=mask)
    result = frame - foreground
    result = np.where(result == 0, background, result)

    cv2.imshow("video", frame)
    cv2.imshow("mask", result)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
