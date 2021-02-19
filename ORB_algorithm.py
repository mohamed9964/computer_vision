import cv2 as cv
img = cv.imread('img2.jpg', cv.IMREAD_GRAYSCALE)
# 1- create object orb
orb = cv.ORB_create(1500)
# 2- detect feature
kp = orb.detect(img, None)
# 3- describe Feature
desc = orb.compute(img, kp)
print(len(kp))
print(orb.descriptorSize())
# 4- draw mark on feature
img2 =cv.drawKeypoints(img, kp, None, (255, 0, 0))
cv.imshow('BRIEF_img', img2)
cv.waitKey()
cv.destroyAllWindows()