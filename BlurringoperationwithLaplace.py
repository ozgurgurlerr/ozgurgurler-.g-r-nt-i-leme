import cv2
import numpy as np

# Load the image
image = cv2.imread('your_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply the Laplacian filter to the blurred image
laplacian = cv2.Laplacian(blurred, cv2.CV_64F)

# Convert the Laplacian result back to uint8
laplacian = np.uint8(np.absolute(laplacian))

# Combine the original image with the Laplacian-filtered image
result = cv2.addWeighted(image, 1.5, cv2.cvtColor(laplacian, cv2.COLOR_GRAY2BGR), -0.5, 0)

# Display the original and result images
cv2.imshow('Original Image', image)
cv2.imshow('Laplacian Blurring Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
