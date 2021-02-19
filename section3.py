# Contours Dtection Shape Analysis, object detection,
# object recognition
import cv2
import numpy as np
img = cv2.imread('open.png')
grayimage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(grayimage, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours "+ str(len(contours)))
cv2.drawContours(img, contours, -1, (0, 255, 0), 4)
cv2.imshow("OrginalImage", img)
cv2.imshow("Gray", grayimage)
# cv2.imshow("thre", thresh)
cv2.waitKey()
cv2.destroyAllWindows()
