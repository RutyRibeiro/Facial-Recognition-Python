import cv2


loadAlgoritmo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread('fotos/imagem1.jpeg')

imagemcinza=cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = loadAlgoritmo.detectMultiScale(imagemcinza)

print(faces)

for(x,y,a,l) in faces:
    cv2.rectangle(imagem,(x,y),(x+l,y+a), (0,255,0), 2)

cv2.imshow('faces', imagem)
cv2.waitKey()

