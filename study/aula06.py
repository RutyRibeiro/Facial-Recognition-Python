import cv2

cam = cv2.VideoCapture(0)
loadFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
loadEyes = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

while True:
    camera,frame = cam.read()

    imgCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detect=loadFace.detectMultiScale(imgCinza)

    for (x, y, a, l) in detect:
        face = cv2.rectangle(frame, (x, y), (x + l, y + a), (0, 255, 0), 2)
        eye = face[y:y + a, x:x + l]
        eyeCinza = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)
        detected = loadEyes.detectMultiScale(eyeCinza)
        for (ox, oy, ol, oa) in detected:
            cv2.rectangle(eye, (ox, oy), (ox + ol, oy + oa), (255, 0, 255), 2)

    cv2.imshow('Câmera', frame)

    if cv2.waitKey(1) == ord('f'):
        break

cam.release()
cv2.destroyAllWindows()