# 高通滤波器（HPF）是检测图像的某个区域，然后根据像素与周围像素的亮度差值来提升
# 该像素的亮度的滤波器。在边缘检测上非常有效。
import cv2
import numpy as np
from scipy import ndimage

kernel_3x3 = np.array([[-1,-1,-1],
                    [-1,8,-1],
                    [-1,-1,-1]])

kernel_5x5 = np.array([[-1,-1,-1,-1,-1],
                    [-1, 1, 2, 1,-1],
                    [-1, 2, 4, 2,-1],
                    [-1, 1, 2, 1,-1],
                    [-1,-1,-2,-1,-1]])

img = cv2.imread("./test_data/2.jpg",0)

k3 = ndimage.convolve(img,kernel_3x3)
k5 = ndimage.convolve(img,kernel_5x5)

# 高斯模糊GaussianBlur，第一个参数是图像，第二个参数是核大小（ksize.width和ksize.height可以不同，但​​它们都必须是正数和奇数）
# 第三个参数是X方向的高斯核标准偏差
blurred = cv2.GaussianBlur(img,(5,5),0)
g_hpf = img - blurred

cv2.imshow("3x3",k3)
cv2.imshow("5x5",k5)
cv2.imshow("blurred",blurred)
cv2.imshow("g_hpf",g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()

