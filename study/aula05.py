import cv2

cam = cv2.VideoCapture(0)
loadAlgoritimo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

while True:
    camera,frame = cam.read()

    imgCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detect=loadAlgoritimo.detectMultiScale(imgCinza)
    for (x, y, a, l) in detect:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (0, 255, 0), 2)

    cv2.imshow('Câmera', frame)

    if cv2.waitKey(1) == ord('f'):
        break
cam.release()
cv2.destroyAllWindows()