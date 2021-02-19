import cv2
import numpy as np
img = cv2.imread("img2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 5)
corners = np.int0(corners)
print(corners)
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 5, (0, 0, 255), -5)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
