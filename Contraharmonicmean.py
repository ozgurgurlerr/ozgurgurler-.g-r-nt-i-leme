import cv2
import numpy as np

def contraharmonic_mean_filter(image, kernel_size, Q):
    # Pad the image to handle border pixels
    padded_image = cv2.copyMakeBorder(image, kernel_size//2, kernel_size//2, kernel_size//2, kernel_size//2, cv2.BORDER_CONSTANT)

    # Create an empty output image
    output_image = np.zeros_like(image, dtype=np.float64)

    for i in range(kernel_size//2, padded_image.shape[0] - kernel_size//2):
        for j in range(kernel_size//2, padded_image.shape[1] - kernel_size//2):
            # Extract the region of interest (ROI) from the padded image
            roi = padded_image[i - kernel_size//2 : i + kernel_size//2 + 1, j - kernel_size//2 : j + kernel_size//2 + 1]

            # Apply the contraharmonic mean formula
            numerator = np.sum(roi**(Q + 1))
            denominator = np.sum(roi**Q)

            # Avoid division by zero
            if denominator != 0:
                output_image[i - kernel_size//2, j - kernel_size//2] = numerator / denominator

    # Clip the values to the valid range [0, 255]
    output_image = np.clip(output_image, 0, 255)

    # Convert the result to uint8
    output_image = np.uint8(output_image)

    return output_image

# Load the image
image = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)

# Define the kernel size and Q parameter
kernel_size = 3
Q = 1.5

# Apply the contraharmonic mean filter
filtered_image = contraharmonic_mean_filter(image, kernel_size, Q)

# Display the original and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Contraharmonic Mean Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()