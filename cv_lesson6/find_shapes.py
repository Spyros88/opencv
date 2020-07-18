import cv2
import imutils
import numpy as np
import argparse

#argument parser
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the image')
args = vars(ap.parse_args())

#load image
image = cv2.imread(args['image'])

#black objects detection
lower = np.array([0, 0, 0])
upper = np.array([15, 15, 15])
shapeMask = cv2.inRange(image, lower, upper)
cv2.imshow('Masked', shapeMask)

#find contours
cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print('found {} object shapes'.format((len(cnts))))

#loop and draw every contour
for c in cnts:
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.imshow('Detected Objects', image)
    cv2.waitKey(0)
