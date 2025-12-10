import cv2
import matplotlib.pyplot as plt
import numpy as np

# Switchung to PyQt based backend due to issues with the default backend on Fedora
# plt.switch_backend('QtAgg')
# ^ Uncomment on Fedora

# Importing an image
img = cv2.imread('../images/image.jpg')

if img is None:
    print("Error: Could not read the image.")
    exit()

# Display the Image
cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Original Histogram of the Image
plt.title('Original Image Histogram')
plt.xlabel('Intensity')
plt.ylabel('Number of Pixels')
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist, color = 'k')
plt.show()

# Histogram Equalization
equ_img = cv2.equalizeHist(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

# Display Equalized Image
cv2.imshow("Equalized Image", equ_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Equalized Histogram
plt.title('Equalized Image Histogram')
plt.xlabel('Intensity')
plt.ylabel('Number of Pixels')
hist_eq = cv2.calcHist([equ_img], [0], None, [256], [0, 256])
plt.plot(hist_eq, color = 'k')
plt.show()


# Histogram Sliding

# Increasing the Brightness
br_img = cv2.add(img, 50)

# Displaying the Brightened Image
cv2.imshow("Brightened Image", br_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Brightened Histogram
plt.title('Brightened Image Histogram')
plt.xlabel('Intensity')
plt.ylabel('Number of Pixels')
hist_br = cv2.calcHist([br_img], [0], None, [256], [0, 256])
plt.plot(hist_br, color = 'k')
plt.show()

# Descreasing the Brightness
dl_img = cv2.subtract(img, 50)

# Displaying the Dulled Image
cv2.imshow("Dulled Image", dl_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Dulled Histogram
plt.title('Dulled Image Histogram')
plt.xlabel('Intensity')
plt.ylabel('Number of Pixels')
hist_br = cv2.calcHist([dl_img], [0], None, [256], [0, 256])
plt.plot(hist_br, color = 'k')
plt.show()
