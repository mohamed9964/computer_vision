import cv2
image = cv2.imread('image.jpg')
cv2.imshow('Orginal Image', image)
# Average
blurImage = cv2.blur(image, (10, 10))
cv2.imshow('average Image', blurImage)
# Gaussian Blur
Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Image', Gaussian)
# Median Blur
median = cv2.medianBlur(image, 5)
cv2.imshow('median Image', median)
# Bilateral Blur
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Bluring', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()