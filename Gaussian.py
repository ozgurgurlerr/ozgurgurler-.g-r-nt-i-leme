import cv2
import numpy as np

# Load the image
image = cv2.imread('your_image.jpg')

# Apply Gaussian blur to the image
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image (Gaussian)', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
