import cv2
from matplotlib import pyplot as plt
img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Perform vertical mirroring
im_flip0 = cv2.flip(img, 0)
# Perform horizontal mirroring
im_flip1 = cv2.flip(img, 1)
plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title('image')
plt.subplot(1, 3, 2), plt.imshow(im_flip0, cmap='gray'), plt.title('vertical')
plt.subplot(1, 3, 3), plt.imshow(im_flip1, cmap='gray'), plt.title('horizontal')
plt.show()