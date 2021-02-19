import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('image.jpg', cv2.COLOR_BGR2RGB)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rows, cols, dim = img.shape
M = np.float32([[1, 0, 100], [0, 1, 100]])
dst = cv2.warpAffine(img, M, (cols, rows))
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('image')
plt.subplot(1, 2, 2), plt.imshow(dst, cmap='gray'), plt.title('translation')
plt.show()
plt.axis('off')