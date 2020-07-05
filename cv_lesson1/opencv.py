import matplotlib.pyplot as plt
import numpy as np
import cv2

print(cv2.__version__)

img = cv2.imread('C:/opencv/opencv-edu/imgs/plateSnow.jpg',1)
output = img.copy()
cv2.rectangle(output, (50, 50), (250, 250), (0, 255, 0), 1)
cv2.imshow("Reactangle", output)
cv2.waitKey(0)
cv2.destroyAllWindows()