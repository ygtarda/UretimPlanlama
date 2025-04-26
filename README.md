📦 Üretim Planlama - Dinamik Programlama Yaklaşımı

📋 Problem Tanımı

Bir üretim hattında n adet iş ve m adet makine bulunmaktadır.
Her işin, her makinede farklı bir işlem süresi vardır.
Makineler arası geçişlerde geçiş maliyetleri oluşmaktadır.
Amaç: İşleri sırayla tamamlamak için minimum toplam süreyi ve minimum geçiş maliyetini bulmaktır.
🔧 Kullanılan Yöntem

Dinamik Programlama yaklaşımı kullanılmıştır.
İşler adım adım değerlendirilerek, her adımda en iyi seçim yapılmıştır.
Tablolama yöntemi ile daha önce bulunan sonuçlar hafızada tutulmuş ve tekrar hesaplama yapılmamıştır.
📈 Zaman ve Uzay Karmaşıklığı

Zaman Karmaşıklığı: O(n × m²)
Uzay Karmaşıklığı: O(n × m)
⚙️ Programın Çalışma Adımları

Kullanıcıdan iş ve makine sayısı alınır.
Her iş için her makinedeki işlem süreleri girilir.
Makineler arası geçiş maliyetleri girilir.
Dinamik programlama tablosu oluşturulur:
Her iş için her makineye ulaşmanın en az maliyetli yolu bulunur.
Minimum toplam süre ve makineler sırası belirlenir.
Sonuçlar kullanıcıya gösterilir:
Minimum süre
Hangi işi hangi makinede yapılacağı
Geçişlerin maliyetleri
▶️ Çalıştırmak İçin

Bilgisayarınızda Python 3 kurulu olmalıdır.

Terminal veya Komut Satırı açılarak şu komutla çalıştırılır:

python üretim_planlama.py
🧪 Test Sonuçları

Örnek bir çalıştırmada:

3 iş ve 2 makine için verilen işlem süreleri ve geçiş maliyetlerine göre;
Program en kısa toplam süreyi ve işlerin makine sıralamasını başarılı bir şekilde bulmuştur.
📽️ Video İçeriği Hakkında

Videoda:

Problem tanımı,
Kullanılan çözüm yöntemi,
Kod yapısının adım adım anlatılması,
Bir örnek çalıştırma ve sonuçların açıklanması, gerekmektedir.
✅ "Şunu yaptım, bunu kullandım" gibi yüzeysel anlatımlar değil; teknik açıklamalar beklenmektedir.

📚 Notlar

Bu proje bireysel çalışma amacıyla yapılmıştır.
Kodlar sade ve anlaşılır yazılmıştır.
Ekstra kütüphane veya ileri seviye modül kullanılmamıştır.
