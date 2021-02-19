import cv2
import numpy as np
# from scipy import ndimage
img = cv2.imread('image.jpg')
blured = cv2.GaussianBlur(img, (75, 75), 0)
g_hpf = img - blured
cv2.imshow("Original", img)
cv2.imshow("bluerImage", blured)
cv2.imshow("g_hpf", g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()