import cv2
import matplotlib.pyplot as plt
# Load image, grayscale, and adaptive threshold
image = cv2.imread('myimage.png')

i = image[210:237,205:223]
# cv2.imshow("myimage",i8)
plt.imshow(i)
cv2.imwrite("4.png",i)
# cv2.waitKey()
plt.show()