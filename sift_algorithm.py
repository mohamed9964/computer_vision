import cv2 as cv
img = cv.imread('img2.jpg', 0)
sift = cv.xfeatures2d.SIFT_create()
kp = sift.detect(img, None)
img1 = cv.drawKeypoints(img, kp, None)
cv.imshow('SIFT', img1)
img2 = cv.drawKeypoints(img, kp, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('SIFT_Enhance', img2)
# To Return Detection and description Feature in img we used function detectAndCompute
kp, desc = sift.detectAndCompute(img, None)
print(kp)
print(desc)
cv.waitKey()
cv.destroyAllWindows()