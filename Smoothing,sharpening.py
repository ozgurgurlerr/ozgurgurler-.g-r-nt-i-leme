import cv2
import numpy as np

# Load the image
image = cv2.imread('your_image.jpg')

# Apply Gaussian blur to the image
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Load the image
image = cv2.imread('your_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Laplacian filter for sharpening
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

# Convert the Laplacian result back to uint8
laplacian = np.uint8(np.absolute(laplacian))

# Combine the original image with the sharpened image
sharpened = cv2.addWeighted(image, 1.5, cv2.cvtColor(laplacian, cv2.COLOR_GRAY2BGR), -0.5, 0)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
