#Normalizasyon:
#Normalizasyon, veri değerlerini belirli bir aralığa dönüştürme işlemidir. Genellikle 0 ile 1 arasında bir değer aralığına getirme işlemidir. Bu, özellikle veri setindeki değerlerin farklı aralıklarda olması durumunda faydalıdır.

#Farklı normalizasyon teknikleri vardır, ancak en yaygın olanı Min-Max Normalizasyon'dur. Bu, veri değerlerini belirli bir aralığa çekmek için kullanılır.
from sklearn.preprocessing import MinMaxScaler

# Örnek veri seti
data = [[1.0, 2.0], [2.0, 3.0], [3.0, 4.0]]

# Min-Max normalizasyonu için scaler oluştur
scaler = MinMaxScaler()

# Veri setini normalizasyon işlemine tabi tut
normalized_data = scaler.fit_transform(data)

print("Normalizasyon sonrası veri:")
print(normalized_data)

#Standardizasyon:
#Standardizasyon, veri değerlerini ortalaması 0, standart sapması 1 olacak şekilde dönüştürme işlemidir. Bu, veri setindeki değerlerin birbirine daha yakın olmasını sağlar.

from sklearn.preprocessing import StandardScaler

# Örnek veri seti
data = [[1.0, 2.0], [2.0, 3.0], [3.0, 4.0]]

# Standardizasyon için scaler oluştur
scaler = StandardScaler()

# Veri setini standardizasyon işlemine tabi tut
standardized_data = scaler.fit_transform(data)

print("Standardizasyon sonrası veri:")
print(standardized_data)

#Bu örneklerde görüldüğü gibi, normalizasyon ve standardizasyon arasındaki temel fark, normalizasyonun veri setini belirli bir aralığa çekmesi, standardizasyonun ise veri setini ortalaması 0 ve standart sapması 1 olacak şekilde dönüştürmesidir. Hangi yöntemin kullanılacağı, veri setinin özelliklerine ve kullanılacak makine öğrenimi modeline bağlıdır.