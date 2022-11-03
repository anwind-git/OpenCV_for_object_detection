import cv2

cap = cv2.VideoCapture('vid.MP4')

while True:
    _, frame = cap.read()
    cv2.imshow("camera", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break