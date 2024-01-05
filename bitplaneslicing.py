#Bit plane slicing, bir resmin her pikselinin bireyliklerini görselleştirmek için kullanılan bir işlemdir. Bu işlem, bir pikselin değerini binary (ikili) formata dönüştürerek her bir bitin temsil ettiği düzeyi görselleştirmeye olanak tanır. Bu sayede bir resmin farklı düzeylerdeki detayları daha iyi anlaşılabilir.
import numpy as np
import cv2
import matplotlib.pyplot as plt

def binary_representation(image):
    # Gri tonlamalı bir resmi ikili forma dönüştür
    binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
    return binary_image

def bit_plane_slicing(image):
    # Resmin ikili gösterimini elde et
    binary_image = binary_representation(image)

    # Resmin boyutları
    height, width = binary_image.shape

    # Bit plane slicing için gerekli olan bit sayısı
    num_bits = 8

    # Her bir bit düzeyini görselleştirmek için alt grafikler oluştur
    fig, axes = plt.subplots(nrows=1, ncols=num_bits, figsize=(15, 3))

    # Her bir bit düzeyini görselleştir
    for i in range(num_bits):
        # 2^i ile AND işlemi uygulanarak belirli bir bitin değeri alınır
        bit_plane = (binary_image & (1 << i)) >> i

        # Alt grafiğe bit düzeyini ekle
        axes[i].imshow(bit_plane, cmap='gray')
        axes[i].set_title(f'Bit {7-i}')

    plt.show()

# Örnek bir resim yükleyelim (örneğin, grayscale bir resim)
image = cv2.imread('example_image.jpg', cv2.IMREAD_GRAYSCALE)

# Bit plane slicing işlemini uygula
bit_plane_slicing(image)
#Bu kod, bir resmin her bir bit düzeyini görselleştirmek için bit plane slicing işlemini gerçekleştirir. binary_representation fonksiyonu, gri tonlamalı bir resmi ikili forma dönüştürür, ardından bit_plane_slicing fonksiyonu, her bir bit düzeyini görselleştirmek için alt grafikler oluşturur.