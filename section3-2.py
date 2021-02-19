import cv2
import numpy as np
img = np.zeros((200, 200), dtype=np.uint8)
img[50:150, 50:150] = 255
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours "+ str(len(contours)))
colorImag = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.drawContours(colorImag, contours, -1, (255, 255, 0), 4)
cv2.imshow("img", img)
cv2.imshow("Colorimg", colorImag)
cv2.waitKey()
cv2.destroyAllWindows()