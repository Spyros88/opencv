import cv2
import numpy as np

#img = np.zeros([512,512,3], np.uint8)
img = cv2.imread('C:\opencv\github\opencv\imgs\tetris_blocks.png' ,1)

#img = cv2.line(img, (0,0) , (200,200), (0,250,0), 10)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()