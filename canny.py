# The Best Filter FOr Edge
import cv2
img = cv2.imread('img.png', 0)
imgCanny = cv2.Canny(img, 200, 300)
cv2.imshow("Canny Image", imgCanny)
cv2.waitKey()
cv2.destroyAllWindows()