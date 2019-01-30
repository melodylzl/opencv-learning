import cv2
import numpy as np

# pyrDown实现的是高斯模糊且下采样
img = cv2.pyrDown(cv2.imread('./test_data/hammer.png',cv2.IMREAD_UNCHANGED))

# 图像二值化
ret,thresh = cv2.threshold(cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY),127,255,cv2.THRESH_BINARY)
# 寻找轮廓
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0))

    # 找出包含点集最小的矩形(可能是旋转的矩形)
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img,[box],0,(0,0,255))

    # 找出最接近点集的圆,返回参数：圆心坐标，半径
    (x,y),radius = cv2.minEnclosingCircle(c)
    center = (int(x),int(y))
    radius = int(radius)
    img = cv2.circle(img,center,radius,(0,255,0))

cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()

