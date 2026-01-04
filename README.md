# SVD ile Görüntü Sıkıştırma (Image Compression with SVD)

<img width="1483" height="791" alt="Ekran görüntüsü 2026-01-04 194401 (1)" src="https://github.com/user-attachments/assets/2b8a3c24-3735-49e3-ab65-72915929abae" />

Bu proje, **Python** ve Doğrusal Cebir yöntemi olan **Singular Value Decomposition (SVD)** kullanarak görüntülerin nasıl sıkıştırılabileceğini ve yeniden oluşturulabileceğini gösterir.

Proje, matris ayrıştırma tekniklerinin görüntü işleme üzerindeki etkisini görselleştirmek amacıyla hazırlanmıştır.

## Proje Hakkında
Görüntüler bilgisayar dünyasında matrisler (sayı tabloları) olarak ifade edilir. SVD yöntemi, bu matrisleri en önemli özelliklerini (tekil değerler) koruyarak daha az veri ile temsil etmemizi sağlar.

Bu repodaki kodlar şu iki temel örneği içerir:
1.  **Yerel Dosya Sıkıştırma:** Bilgisayarınızdaki bir fotoğrafı yükleyip belirli bir sıkıştırma oranıyla (k değeri) yeniden oluşturma.
2.  **Karşılaştırmalı Analiz:** İnternetten bir görsel çekip, 4 farklı kalite seviyesinde (k=5, 20, 50, 100) yan yana karşılaştırma.

##  Kurulum

Projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız vardır:

* NumPy (Matris işlemleri için)
* Matplotlib (Görselleştirme için)
* Scikit-Image (Görüntü işleme ve yükleme için)

Gerekli paketleri yüklemek için terminale şu komutu yazabilirsiniz:
  ```bash
  pip install numpy matplotlib scikit-image
