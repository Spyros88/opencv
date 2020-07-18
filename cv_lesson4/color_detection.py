import cv2 
import numpy as np
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', help = 'path to the image' )
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
small = imutils.resize(image, width=400)
cv2.imshow('image', small)

# define the list of boundaries
boundaries = [
	([17, 17, 129], [101, 101, 255]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([32, 111, 85], [85, 247, 193])
]
boundaries_tennis_ball = [
     #B   #G   #R   #B   #G   #R
	([0, 112, 101], [84, 255, 235]) #green tennis ball
]

#loop for every item in list
for (lower, upper) in boundaries:
    #create numpy arrays from the boundaries
    lower = np.array(lower, dtype= 'uint8')
    upper = np.array(upper, dtype= 'uint8')

    #find the colors wihin the specified boundaries and apply the mask
    mask = cv2.inRange(small, lower, upper)
    output = cv2.bitwise_and(small, small, mask = mask)

    cv2.imshow('output', np.hstack([small, output]))
    cv2.waitKey(0)