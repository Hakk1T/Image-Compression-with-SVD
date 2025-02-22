# 1. Ornek

import numpy as np                  # Matris işlerini yapmamız için gerekli
import matplotlib.pyplot as plt     # Görüntüeri yazdırmamız için gereki
from skimage import color, io       # Görüntüyü yüklemek ve gri tonlamaya çevirmek için gerekli 

resim = io.imread("ornek_resim.jpg")
gri_resim = color.rgb2gray(resim)

U, Sigma2, Vt2 = np.linalg.svd(gri_resim, full_matrices=False)

k = 50
compressed1 = (U[:,:k] @ np.diag(Sigma2[:k]) @ Vt2[:k,:])

plt.figure(figsize=(5,5))
plt.imshow(compressed1, cmap="gray")    # cmap="gray" komutunu kullanmamızın sebebi görüntüyü gray olarak oluşturduk eğer komutu kaldırırsak matplot renkleri 
plt.axis= ("off")                       # yanlış yorumlayarak rengi bozuk bir görüntü elde ederiz 
plt.show()

# 2. Ornek

# 1. Görüntüyü yükle ve gri tonlamaya kısmı 
# io.imread görüntüyü okumak veya indirmek için gereklidir 
image = io.imread('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Example.jpg/512px-Example.jpg')
gray_image = color.rgb2gray(image)

# 2. SVD Ayrıştırması
# Görüntünün u, sigma ve vt değerlerine ayrıştılır ve full_matrices kullanmamızın sebebi gereksiz büyük matris oluşturmayı engellemek içindir 
U, S, Vt = np.linalg.svd(gray_image, full_matrices=False)

# 3. Farklı tekil değerlerle görüntüyü yeniden oluştur
# fig tüm ana grafik alanını temsil eder, axes ise 4 farklı alt grafiği temsil eder, subplots satır ve sütun sayısını temsil eder, figsize grafik boyutunu temsil eder 
fig, axes = plt.subplots(1, 4, figsize=(15, 5))

# 4. Farklı sayıda tekil değer kullanarak görüntüleri yeniden oluşturma kısmı 
# for döngüsü ile sırasıyla k değerleriyle görüntüleri oluştururuz 
# enumerate indeks ve değeri aynı anda almamızı sağlar 
for i, k in enumerate([5, 20, 50, 100]):
    # [:, :] ifadesi numpy da matrislerde istediğim sayısal veriyi almamızı sağlar, örnek olarak [:, :k] tüm satırlardan k. sütununu seç demektir
    compressed = (U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :])
    axes[i].imshow(compressed, cmap='gray')
    axes[i].set_title(f'k = {k}')
    axes[i].axis('off')

plt.show()