import cv2
import matplotlib.pyplot as plt
# Load image, grayscale, and adaptive threshold

image = cv2.imread('live.png')

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



i = image[210:240,180:250]
# cv2.imshow("myimage",i)
plt.imshow(i)
cv2.imwrite("2408.png",i)
# cv2.waitKey()
plt.show()
