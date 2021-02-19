import cv2
import numpy as np
img = cv2.imread("img2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
corners = cv2.cornerHarris(gray, 2, 3, 0.04)

# Result is dilated for ((MARKING the corners)), not important
corners = cv2.dilate(corners, None)
# Threshold for an optimal value, it may vary depending on the image
threshold = corners > 0.01 * corners.max()
img[threshold] = [0, 0, 255]
cv2.imshow("image", img)
# cv2.imshow("image_gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
