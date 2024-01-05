import cv2
import numpy as np

def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)

    # Salt noise
    salt_mask = np.random.rand(*image.shape[:2]) < salt_prob
    noisy_image[salt_mask] = 255

    # Pepper noise
    pepper_mask = np.random.rand(*image.shape[:2]) < pepper_prob
    noisy_image[pepper_mask] = 0

    return noisy_image

# Load the image
image = cv2.imread('your_image.jpg')

# Define the probabilities for salt and pepper noise
salt_probability = 0.02  # Adjust based on your preference
pepper_probability = 0.02  # Adjust based on your preference

# Add salt and pepper noise to the image
noisy_image = add_salt_and_pepper_noise(image, salt_probability, pepper_probability)

# Display the original and noisy images
cv2.imshow('Original Image', image)
cv2.imshow('Noisy Image (Salt and Pepper)', noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
