#Gamma düzeltme veya gamma ayarı, bir görüntünün parlaklık ve kontrastını değiştirmek için kullanılan bir yöntemdir. Gamma düzeltme, bir pikselin intensitesini şu formülle ayarlar:Burada, γ parametresi, pozitif bir gerçek sayıdır.γ değeri 1'e yaklaştıkça, görüntü orijinal haline yaklaşır.γ değeri 1'den küçükse, görüntü daha karanlık hale gelir;γ değeri 1'den büyükse, görüntü daha parlak hale gelir.

import cv2
import numpy as np
import matplotlib.pyplot as plt

def gamma_correction(image, gamma=1.0):
    # Görüntüdeki piksel değerlerini gamma ile güncelle
    corrected_image = np.power(image/255.0, gamma) * 255.0

    # Piksel değerlerini integer'a çevir
    corrected_image = np.round(corrected_image).astype(np.uint8)

    return corrected_image

# Örnek bir resim yükleyelim (örneğin, grayscale bir resim)
image = cv2.imread('example_image.jpg', cv2.IMREAD_GRAYSCALE)

# Gamma düzeltme işlemini uygula (örneğin, gamma=0.5)
gamma_value = 0.5
gamma_corrected_image = gamma_correction(image, gamma_value)

# Orjinal ve gamma düzeltme sonrası resimleri görselleştir
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap='gray')
axes[0].set_title('Orjinal Resim')

axes[1].imshow(gamma_corrected_image, cmap='gray')
axes[1].set_title(f'Gamma Düzeltme (Gamma={gamma_value})')

for ax in axes:
    ax.axis('off')

plt.show()

#Bu örnek kodda, gamma_correction fonksiyonu, görüntüdeki piksel değerlerini belirli bir gamma değeri ile günceller. Bu güncelleme, görüntünün parlaklık ve kontrastını değiştirmek için kullanılır. gamma_value parametresini farklı değerlerle deneyerek görüntüdeki değişiklikleri gözlemleyebilirsiniz.
