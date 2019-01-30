import cv2
import numpy as np

img = cv2.imread('./test_data/2.jpg',0)
# canny边缘检测，第二、第三个参数是双阀值
cannyImg = cv2.Canny(img,200,300)
cv2.imshow("img",img)
cv2.imshow("cannyImg",cannyImg)
cv2.waitKey()
cv2.destroyAllWindows()
