import cv2
from matplotlib import pyplot as plt
img = cv2.imread('image.jpg', 0)
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('image')
###
im_equ = cv2.equalizeHist(img)
plt.subplot(2, 2, 2)
plt.hist(img.ravel(), 256, [0, 256], label='org')
###
plt.subplot(2, 2, 3)
plt.imshow(im_equ, cmap='gray')
plt.title('image_hist')
plt.subplot(2, 2, 4)
plt.hist(im_equ.ravel(), 256, [0, 256], label='equalize')
plt.show()


