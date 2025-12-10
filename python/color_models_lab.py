import cv2
import matplotlib.pyplot as plt

# Switchung to PyQt based backend due to issues with the default backend on Fedora
# plt.switch_backend('QtAgg')
# ^ Uncomment on Fedora

# Importing an image
img = cv2.imread('../images/image.jpg')

# Converting to different color models
rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Displaying the images and histograms

# Base image
cv2.imshow("Base Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Histogram
plt.title('Base Image')
plt.xlabel('Intensity')
plt.ylabel('Number of Pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = col)
plt.show()

# RGB Image
cv2.imshow("RGB Image", rgb_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Histogram
plt.title('RGB Image')
plt.xlabel('Intensity')
plt.ylabel('Number of Pixels')
colors = ('r', 'g', 'b')
for i, col in enumerate(colors):
    hist = cv2.calcHist([rgb_image], [i], None, [256], [0, 256])
    plt.plot(hist, color = col)
plt.show()

# HSV Image
cv2.imshow("HSV Image", hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Histogram
plt.title('HSV Image')
plt.xlabel('Intensity')
plt.ylabel('Number of Pixels')
channels = ('Hue', 'Saturation', 'Value')
colors = ('r', 'g', 'b')
for i, (chan, col) in enumerate(zip(channels, colors)):
    hist = cv2.calcHist([hsv_image], [i], None, [256], [0, 256])
    plt.plot(hist, color = col, label=chan)
plt.show()

# RGB Image
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Histogram
plt.title('Grayscale Image')
plt.xlabel('Intensity')
plt.ylabel('Number of Pixels')
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
plt.plot(hist, color = 'k')
plt.show()
