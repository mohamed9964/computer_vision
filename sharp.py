
import cv2
import numpy as np
# from scipy import ndimage
img = cv2.imread('image.jpg')
# smooth filter
kernal1 = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                    [0.04, 0.04, 0.04, 0.04, 0.04],
                    [0.04, 0.04, 0.04, 0.04, 0.04],
                   [0.04, 0.04, 0.04, 0.04, 0.04]])
smooth = cv2.filter2D(img, -1, kernal1)
cv2.imshow("Smooth Image", smooth)
# sharp filter
kernal2 = np.array([[-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1]])
SharpImage = cv2.filter2D(img, -1, kernal2)
cv2.imshow("Sharp Image", SharpImage)
# sharpImage2= ndimage.convolve(img, kernal2)
# cv2.imshow('Sharpp', sharpImage2)
cv2.waitKey()
cv2.destroyAllWindows()