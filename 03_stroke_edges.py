import cv2
import numpy

def strokeEdges(src, dst, blurKsize = 7, edgeKsize = 5):
    if blurKsize >= 3 :
        blurredSrc = cv2.medianBlur(src, blurKsize)
        graySrc = cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY)
    else:
        graySrc = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
    #边缘检测滤波算法    
    cv2.Laplacian(graySrc,cv2.CV_8U,graySrc,ksize = edgeKsize)
    normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc)
    channels = cv2.split(src)
    for channel in channels:
        channel[:] = channel * normalizedInverseAlpha
    cv2.merge(channels,dst)

img = cv2.imread('./test_data/2.jpg')
strokeEdges(img,img)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()

