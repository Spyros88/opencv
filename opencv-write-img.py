import cv2
import numpy as np

img = cv2.imread('c:\opencv\zcoin.jpg' ,1)

img = cv2.line(img, (0,0) , (200,200), (0,250,0), 10)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()