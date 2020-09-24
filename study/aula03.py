import cv2

loadface = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
loadeyes = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

imagem = cv2.imread('fotos/imagem1.jpeg')
imagemCinza=cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
faces = loadface.detectMultiScale(imagemCinza)

for(x, y, l, a) in faces:
    imagem = cv2.rectangle(imagem, (x,y), (x+l, y+a), (255,0,255), 2)
    eye = imagem[y:y + a, x:x + l]
    eyeCinza = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)
    detected = loadeyes.detectMultiScale(eyeCinza)

    for(ox,oy,ol,oa) in detected:
        cv2.rectangle(eye, (ox,oy), (ox+ol, oy+oa), (255,0,255), 2)
cv2.imshow('Detecta face e olhos', imagem)
cv2.waitKey()