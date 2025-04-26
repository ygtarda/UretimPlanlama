# 📦 Dinamik Programlama ile Üretim Planlama

Bu projede, bir üretim hattındaki işlerin farklı makinelerde minimum süre ve maliyetle tamamlanması amaçlanmıştır.

---

## 📚 Problem Tanımı

- Bir üretim hattında, **n adet iş** ve **m adet makine** bulunmaktadır.
- Her işin, her makinedeki işlem süresi farklıdır.
- İşler sırayla yapılmalı ve makineler arasında geçişlerde bir maliyet oluşmaktadır.
- Amaç, işleri sırasıyla en az toplam süre ve maliyetle tamamlamaktır.

---

## 🔗 Problem Tanımı ve Matris Zinciri Çarpımı ile İlişkisi

Bu problem, matris zinciri çarpımı problemine benzer şekilde ardışık kararlar vererek en düşük toplam maliyeti bulmayı hedefler.  
Her iş için en uygun makine seçimi yapılırken, bir önceki makineden geçiş maliyeti de dikkate alınır.  
Dinamik programlama ile geçmiş adımlar göz önünde bulundurularak minimum toplam süre hesaplanır.

---

## 🛠️ Kullanılan Yöntem

- **Dinamik Programlama** yaklaşımı kullanılmıştır.
- Her iş için her makinede minimum süre ve maliyet hesaplanmıştır.
- Önceki makine seçimleri ve geçiş maliyetleri dikkate alınarak tablo doldurulmuştur.

---

## ⏱️ Zaman ve Uzay Karmaşıklığı

- **Zaman Karmaşıklığı:** O(n × m²)
- **Uzay Karmaşıklığı:** O(n × m)

Burada:
- **n:** İş sayısı
- **m:** Makine sayısıdır.

---

## 🧩 Kodun Özeti

- Kullanıcıdan iş ve makine sayısı, işlem süreleri ve geçiş maliyetleri alınır.
- Dinamik programlama tablosu oluşturulur.
- Her adımda minimum toplam süre ve geçiş bilgileri hesaplanır.
- Minimum toplam süre ve hangi işin hangi makinede yapıldığı bulunur.
- Sonuçlar detaylı şekilde ekrana yazdırılır.

---

## ▶️ Projeyi Çalıştırmak İçin

Python 3 yüklü olmalıdır.  
Terminal veya komut satırında aşağıdaki komutu çalıştırabilirsiniz:

```bash
python üretim_planlama.py
```

---

## ✅ Test Sonuçları

Örnek bir çalıştırma:

```
Kaç iş var? 4
Kaç makine var? 2

İşlem sürelerini giriniz:
İş 1 - Makine 1 işlem süresi: 30
İş 1 - Makine 2 işlem süresi: 50
İş 2 - Makine 1 işlem süresi: 30
İş 2 - Makine 2 işlem süresi: 40
İş 3 - Makine 1 işlem süresi: 60
İş 3 - Makine 2 işlem süresi: 80
İş 4 - Makine 1 işlem süresi: 20
İş 4 - Makine 2 işlem süresi: 12

Geçiş maliyetlerini giriniz:
Makine 1 -> Makine 1 geçiş maliyeti: 5
Makine 1 -> Makine 2 geçiş maliyeti: 6
Makine 2 -> Makine 1 geçiş maliyeti: 7
Makine 2 -> Makine 2 geçiş maliyeti: 8

---

🔵 Minimum Toplam Süre: 148

İşlerin Sırası ve Kullanılan Makineler:
İş 1: Makine 1
İş 2: Makine 1
İş 3: Makine 1
İş 4: Makine 2

Geçişler:
Makine 1 -> Makine 1 (Maliyet: 5)
Makine 1 -> Makine 1 (Maliyet: 5)
Makine 1 -> Makine 2 (Maliyet: 6)

🟢 Toplam Geçiş Maliyeti: 16
```

---

## 🎥 Demo Videosu

(Kendi anlatımınızla hazırlayacağınız proje videosunu buraya ekleyiniz.)

---

## 📎 Notlar

- Bu proje, "Dinamik Programlama Yaklaşımı ile Üretim Planlama" ödevi kapsamında hazırlanmıştır.
- Python programlama dili kullanılmıştır.
- Video anlatımı zorunludur. (Şu an video henüz eklenmemiştir.)

---
