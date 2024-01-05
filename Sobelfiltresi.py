import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü yükle
image = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)

# Sobel filtresini uygula
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Gradient büyüklüğünü hesapla
gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

# Görüntü ve Sobel sonuçlarını göster
plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 2, 2)
plt.imshow(np.abs(sobel_x), cmap='gray')
plt.title('Sobel X')

plt.subplot(2, 2, 3)
plt.imshow(np.abs(sobel_y), cmap='gray')
plt.title('Sobel Y')

plt.subplot(2, 2, 4)
plt.imshow(gradient_magnitude, cmap='gray')
plt.title('Gradient Magnitude')

plt.tight_layout()
plt.show()
