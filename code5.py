import cv2
import numpy as np
originalImage = cv2.imread('image.jpg')
hsvImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2HSV)
cv2.imshow("Orginal", originalImage)

lower = np.array([0, 100, 100])
upper = np.array([10, 255, 255])
mask = cv2.inRange(hsvImage, lower, upper)
shape = cv2.bitwise_and(originalImage,originalImage, mask=mask)
cv2.imshow("MASK", mask)
cv2.imshow("Orange_shape", shape)
cv2.waitKey()
cv2.destroyAllWindows()
