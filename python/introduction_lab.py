import cv2
import matplotlib.pyplot as plt

# Switchung to PyQt based backend due to issues with the default backend on Fedora
plt.switch_backend('QtAgg')

img = cv2.imread('../images/image1.JPG') # The folder isn't pushed to the repo

cv2.imshow('Image using OpenCV', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Image using Matplotlib')
plt.show()

cv2.imshow('Grayscale Image using OpenCV', cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cmap='gray')
plt.title('Grayscale Image using Matplotlib')
plt.show()
