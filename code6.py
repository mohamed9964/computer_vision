import cv2
import numpy as np
originalImage = cv2.imread('image.jpg')
half = cv2.resize(originalImage, (0, 0), fx=.5, fy=.5)
bigger = cv2.resize(originalImage, (700, 1200))
half = cv2.resize(originalImage, (0, 0), fx=.5, fy=.5)
stretch_near = cv2.resize(originalImage, (700, 1200),
                          interpolation= cv2.INTER_NEAREST)
cv2.imshow("HalfImage", half)
cv2.imshow("stretchNearImage", stretch_near)
cv2.imshow("BiggerImage", bigger)
cv2.waitKey()
cv2.destroyAllWindows()
