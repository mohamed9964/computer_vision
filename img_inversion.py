import cv2
from matplotlib import pyplot as plt
img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = 255 - img
img_not = cv2.bitwise_not(img)
plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title('image')
plt.subplot(1, 3, 2), plt.imshow(img2, cmap='gray'), plt.title('invert1')
plt.subplot(1, 3, 3), plt.imshow(img_not, cmap='gray'), plt.title('invert2')
plt.show()