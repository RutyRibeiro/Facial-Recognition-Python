import cv2

loadAlgoritimo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread('fotos/imagem1.jpeg')

imagemCinza=cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

faces = loadAlgoritimo.detectMultiScale(imagemCinza, scaleFactor=1.08)

print(faces)

for(x, y, l, a) in faces:
    cv2.rectangle(imagem, (x,y), (x+l, y+a), (255,0,255), 2)

cv2.imshow('faces', imagem)
cv2.waitKey()