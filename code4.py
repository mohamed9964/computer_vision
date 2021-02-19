import cv2
originalImage = cv2.imread('image.jpg')
hsvImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2HSV)

###
# B, G, R = cv2.split(originalImage)
# cv2.imshow("b", B)
# cv2.imshow("g", G)
# cv2.imshow("r", R)
# mergeImage = cv2.merge((B, G, R))
# cv2.imshow('mergeImage', mergeImage)
# mergeImage2 = cv2.merge((R, G, B))
# cv2.imshow('mergeImage2', mergeImage2)
###

h = hsvImage[:, :, 0]
s = hsvImage[:, :, 1]
v = hsvImage[:, :, 2]
cv2.imshow('HSV', hsvImage)
cv2.imshow('HUE', h)
cv2.imshow('saturation', s)
cv2.imshow('value', v)
mergeImage = cv2.merge((v, s, h))
cv2.imshow('mergeImage', mergeImage)
cv2.waitKey()
cv2.destroyAllWindows()