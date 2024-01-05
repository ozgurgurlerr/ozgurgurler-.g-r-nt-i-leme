import cv2
import numpy as np

# Açma işlemi (Opening)
def opening(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    opening_result = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    return opening_result

# Kapanma işlemi (Closing)
def closing(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    closing_result = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return closing_result

# Load the image
image = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)

# Define the kernel size
kernel_size = 5

# Apply opening operation
opened_image = opening(image, kernel_size)

# Apply closing operation
closed_image = closing(image, kernel_size)

# Display the original, opened, and closed images
cv2.imshow('Original Image', image)
cv2.imshow('Opened Image', opened_image)
cv2.imshow('Closed Image', closed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()