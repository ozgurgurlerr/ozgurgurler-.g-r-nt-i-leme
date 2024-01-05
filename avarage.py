#Ortalama filtresi (Mean Filter), bir görüntü üzerindeki gürültüyü azaltmak veya yumuşatmak amacıyla kullanılan bir düşük geçiren (low-pass) filtre türüdür. Bu filtre, bir pikselin değerini, kendisi ve çevresindeki piksellerin ortalaması ile değiştirir. Genellikle, bu tür filtrelerin kullanılması, görüntüdeki küçük detayları ve gürültüyü azaltmak için tercih edilir.Ortalama filtresi, bir görüntü üzerinde kayma penceresi tekniği kullanılarak uygulanır. Pencere, her bir pikselin etrafındaki belirli bir bölgeyi kapsar, ve bu bölge içindeki piksel değerlerinin ortalaması alınarak o pikselin değeri ile değiştirilir.
import cv2
import numpy as np
import matplotlib.pyplot as plt

def mean_filter(image, kernel_size):
    # Görüntüyü gri tonlamalı hale getir (renkli görüntü ise kanalları ayırmak gerekebilir)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Görüntüyü belirtilen kernel boyutunda bir ortalamalı filtreden geçir
    filtered_image = cv2.blur(gray_image, (kernel_size, kernel_size))

    return filtered_image

# Örnek bir resim yükleyelim
image = cv2.imread('example_image.jpg')

# Ortalamalı filtre uygula
kernel_size = 5  # Filtre boyutu
filtered_image = mean_filter(image, kernel_size)

# Orjinal ve filtrelenmiş resimleri görselleştir
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0].set_title('Orjinal Resim')

axes[1].imshow(filtered_image, cmap='gray')
axes[1].set_title('Ortalama Filtreleme Sonrası')

for ax in axes:
    ax.axis('off')

plt.show()
#Bu örnekte, mean_filter fonksiyonu, belirli bir kernel boyutunda ortalama filtreleme işlemini uygular. cv2.blur fonksiyonu kullanılarak görüntüyü filtrelenmiş hale getirir. 

