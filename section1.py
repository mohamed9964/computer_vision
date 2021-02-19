import numpy as np
import cv2
'''
# create a 3x3 square black image using a 2D numpy array
img1 = np.zeros((3, 3), dtype=np.uint8)
print('img1 =', img1)
print('\n')

# convert this image into blue-green-red (BGR) format using the cv2cvtColor function
img2 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
print("img2 = \n", img2)
print('\n')

# the structure of an image by inspecting the shape property, which returns row, columns and number of channels
img3 = np.zeros((5, 3), dtype=np.uint8)
print(img3.shape)
print('\n')

# convert this image into blue-green-red (BGR) format using the cv2cvtColor function
img4 = cv2.cvtColor(img3, cv2.COLOR_GRAY2BGR)
print(img4.shape)
print('\n')
'''
img = cv2.imread('1234.jpg', cv2.IMREAD_REDUCED_GRAYSCALE_8)
# cv2.imwrite(r'D:\Mypic.jpg', img)
cv2.imshow('image', img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
