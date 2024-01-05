import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü yükle
image = cv2.imread('your_image.jpg')

# Gaussian filtresini uygula
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Görüntü ve Gaussian filtresi sonuçlarını göster
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.title('Blurred Image (Gaussian)')

plt.tight_layout()
plt.show()