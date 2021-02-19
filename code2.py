'''
filter is two types :
-> low pass filter (lpf) such as blur and smooth filter
-> heigh pass filter (hpf) such as sharp and edge detection
'''
import cv2
import numpy
grayImage = numpy.random.randint(0, 256, 120000).reshape(300, 400)
cv2.imwrite('RandomGray.png', grayImage)
bgrImage = numpy.random.randint(0, 256, 120000).reshape(100, 400, 3)
cv2.imwrite('RandomColor.png', bgrImage)
