import cv2
import numpy as np

img = np.zeros((200,200),dtype=np.uint8)
img[50:150,50:150] = 255

# 图像二值化
ret,thresh = cv2.threshold(img,127,255,0)
# 寻找轮廓
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
color = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)
# 绘制轮廓drawContours 第一个参数输入图像，第二个参数轮廓数据
# 第三个参数-1 表示绘制所有轮廓,第四个参数轮廓的颜色，第五个参数轮廓的粗细
img = cv2.drawContours(color,contours,-1,(0,255,0),2)

cv2.imshow('drawContours',img)
cv2.waitKey()
cv2.destroyAllWindows()