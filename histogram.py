#Histogram eşitleme, bir görüntünün piksel yoğunluklarını daha geniş bir aralığa yayarak kontrastı artıran bir işlemdir. Bu işlem, bir görüntünün daha iyi görüntülenmesini sağlamak ve daha iyi analiz yapılmasına yardımcı olmak amacıyla kullanılır. Histogram eşitleme, özellikle düşük kontrastlı görüntülerde ve belirli aydınlatma koşullarında etkili bir iyileştirme sağlar.
import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(image):
    # Gri tonlamalı bir resmi histogram eşitleme işlemine tabi tut
    equalized_image = cv2.equalizeHist(image)
    return equalized_image

# Örnek bir resim yükleyelim (örneğin, grayscale bir resim)
image = cv2.imread('example_image.jpg', cv2.IMREAD_GRAYSCALE)

# Histogram eşitleme işlemini uygula
equalized_image = histogram_equalization(image)

# Orjinal ve eşitleme sonrası resimleri görselleştir
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap='gray')
axes[0].set_title('Orjinal Resim')

axes[1].imshow(equalized_image, cmap='gray')
axes[1].set_title('Histogram Eşitleme Sonrası')

for ax in axes:
    ax.axis('off')

plt.show()
#Bu kod örneğinde, cv2.equalizeHist fonksiyonu kullanılarak histogram eşitleme işlemi uygulanmaktadır. Orjinal gri tonlamalı resim ve histogram eşitleme sonrası elde edilen resim yan yana görselleştirilmiştir.