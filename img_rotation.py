import cv2
from matplotlib import pyplot as plt
img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rows, cols, dim = img.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('image')
plt.subplot(1, 2, 2), plt.imshow(dst, cmap='gray'), plt.title('translation')
plt.show()
plt.axis('off')
plt.imsave('rotated_img', dst)