import cv2
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help='path to input image')
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])
cv2.imshow("Image", image)

#convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray' , gray)
#edge detection
edged = cv2.Canny(gray, 30, 150)
cv2.imshow('Edged', edged)
#apply threshold
thresh = cv2.threshold(gray, 235, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnts = imutils.grab_contours(cnts)
output = image.copy()
#draw contours
for c in cnts:
    cv2.drawContours(output, [c], -1, (255, 0, 0), 2)
# write number of contours
text = "Found {} objects".format(len(cnts))
cv2.putText(output, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7 , (255, 0, 145), 2)
cv2.imshow("Contours", output)
#exit with any keypress
cv2.waitKey(0)