import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('abba.png')
cv2.imshow('original Image', img)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, 1.1)
for(x, y, w, h) in faces:
    cv2.circle(img, (np.int0(x + w/2), np.int0(y+h/2)), np.int0(w/2), (255, 0, 0), 2)
cv2.imshow('DetectFaces', img)
cv2.waitKey()
cv2.destroyAllWindows()
