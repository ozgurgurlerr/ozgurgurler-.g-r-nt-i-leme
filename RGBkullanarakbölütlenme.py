import cv2
import numpy as np

def segment_by_color(image, lower_threshold, upper_threshold):
    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the red color in HSV
    lower_bound = np.array(lower_threshold, dtype=np.uint8)
    upper_bound = np.array(upper_threshold, dtype=np.uint8)

    # Create a binary mask using inRange function
    color_mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    # Apply the mask to the original image
    segmented_image = cv2.bitwise_and(image, image, mask=color_mask)

    return segmented_image

# Load the image
image = cv2.imread('your_image.jpg')

# Define the lower and upper bounds for red color in RGB
lower_red = [0, 0, 100]
upper_red = [100, 100, 255]

# Perform segmentation based on red color
segmented_image = segment_by_color(image, lower_red, upper_red)

# Display the original and segmented images
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image (Red)', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
