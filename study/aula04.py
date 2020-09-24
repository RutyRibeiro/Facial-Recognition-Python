import cv2

cam = cv2.VideoCapture(0)

while True:
    camera,frame = cam.read()
    cv2.imshow('imagem camera', frame)

    if cv2.waitKey(1) == ord('f'):
        break
cam.release()
cv2.destroyAllWindows()