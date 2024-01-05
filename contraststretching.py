#Contrast stretching, bir görüntünün kontrastını artırmak için kullanılan bir işlemdir. Bu işlemde, görüntünün piksel değerleri belirli bir aralığa genişletilir, bu da görüntüdeki renk farklılıklarını daha belirgin hale getirir. Contrast stretching, özellikle bir görüntüdeki düşük kontrastlı bölgeleri vurgulamak ve görsel analiz için daha iyi bir görüntü elde etmek amacıyla kullanılır.
import cv2
import numpy as np
import matplotlib.pyplot as plt

def contrast_stretching(image, min_out=0, max_out=255):
    # Görüntüdeki piksel değerlerini normalleştir
    min_in, max_in = np.min(image), np.max(image)
    
    # Contrast stretching formülü
    stretched_image = ((image - min_in) / (max_in - min_in)) * (max_out - min_out) + min_out

    # Piksel değerlerini integer'a çevir
    stretched_image = np.round(stretched_image).astype(np.uint8)

    return stretched_image

# Örnek bir resim yükleyelim (örneğin, grayscale bir resim)
image = cv2.imread('example_image.jpg', cv2.IMREAD_GRAYSCALE)

# Contrast stretching işlemini uygula
stretched_image = contrast_stretching(image)

# Orjinal ve contrast stretching sonrası resimleri görselleştir
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap='gray')
axes[0].set_title('Orjinal Resim')

axes[1].imshow(stretched_image, cmap='gray')
axes[1].set_title('Contrast Stretching Sonrası')

for ax in axes:
    ax.axis('off')

plt.show()
#Bu örnek kodda, contrast_stretching fonksiyonu görüntüdeki piksel değerlerini belirli bir aralığa genişletir. Bu genişletme, orijinal görüntüdeki kontrastı artırır ve daha belirgin bir görüntü elde edilmesine katkıda bulunur. Contrast stretching işlemi, genellikle görüntü iyileştirme ve analiz uygulamalarında kullanılır.