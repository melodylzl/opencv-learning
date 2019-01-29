import cv2
from matplotlib import pyplot as plt

image = cv2.imread('./test_data/1.jpg',cv2.IMREAD_GRAYSCALE)
ret = cv2.imwrite('./test_data/1_out.png',image)
print("imwrite ret",ret)

plt.imshow(image)
plt.show()