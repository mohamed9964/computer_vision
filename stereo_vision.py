import cv2
import numpy as np

minDisparity = 16
numDisparities = 192 - minDisparity
blockSize = 5
# p1, p2 parameter controlling the disparity smoothness
p1 = 600
p2 = 2400
# SGBM stands for semi-global block matching
stereo = cv2.StereoSGBM_create(minDisparity=minDisparity,
                               numDisparities=numDisparities,
                               blockSize=blockSize,
                               P1=p1, P2=p2)

imgL = cv2.imread('color1_small.jpg')
imgR = cv2.imread('color2_small.jpg')


def update():
    stereo.setBlockSize(cv2.getTrackbarPos('blockSize', 'DisparityView'))


disparity = stereo.compute(imgL, imgR).astype(np.float32) / 16.0
cv2.imshow('LeftView', imgL)
cv2.imshow('RightView', imgR)
cv2.imshow('DisparityView', (disparity - minDisparity) / numDisparities)

cv2.namedWindow('DisparityView')
cv2.createTrackbar('blockSize', 'DisparityView', blockSize, 21, update)

update()
cv2.waitKey()
cv2.destroyAllWindows()
