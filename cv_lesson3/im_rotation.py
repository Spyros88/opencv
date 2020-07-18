import numpy as np
import cv2
import imutils
import argparse

#arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image file")
args = vars(ap.parse_args())

#load image
image = cv2.imread(args['image'])
(h, w) = image.shape[:2]
small = imutils.resize(image, int(w/2))
#print(small.shape[:2])
# for angle in np.arange(0, 360, 15):
#     rotated = imutils.rotate(small, angle)
#     cv2.imshow('rotated1', rotated)
#     cv2.waitKey(0)

# for angle in np.arange(0, 360, 15):
#     rotated = imutils.rotate_bound(small, angle)
#     cv2.imshow('rotated imutils', rotated)
#     cv2.waitKey(0)
gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
cv2.waitKey(0)

gray = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(gray, 20, 100)
cv2.imshow('Edged', edged)
cv2.waitKey(0)