# 📦 Dinamik Programlama ile Üretim Planlama

Bu projede, bir üretim hattındaki işlerin farklı makinelerde minimum süre ve maliyetle tamamlanması amaçlanmıştır.

---

## 📚 Problem Tanımı

- n adet iş ve m adet makine vardır.
- Her işin her makinede farklı işlem süresi vardır.
- Makineler arasında geçiş maliyetleri bulunmaktadır.
- Amaç, işleri sırayla tamamlamak için **minimum toplam süreyi** bulmaktır.

---

## ⚙️ Kullanılan Yöntem

- **Dinamik Programlama** yaklaşımı kullanılmıştır.
- Her iş için en iyi makine seçimi yapılmıştır.
- Geçiş maliyetleri dikkate alınarak toplam süre hesaplanmıştır.

**Zaman Karmaşıklığı:** O(n × m²)  
**Uzay Karmaşıklığı:** O(n × m)

---

## 🧩 Kodun Özeti

- Kullanıcıdan işlem süreleri ve geçiş maliyetleri alınır.
- Dinamik programlama tablosu oluşturulur.
- Minimum süre ve en uygun makine sırası bulunur.
- Sonuçlar ekrana açıklayıcı şekilde yazdırılır.

---

## 🚀 Çalıştırmak İçin

Python 3 yüklü olması gereklidir. Çalıştırmak için terminal veya komut satırına şunu yazın:

```bash
python üretim_planlama.py
