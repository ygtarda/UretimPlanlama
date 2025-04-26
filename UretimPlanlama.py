def main():
    print("=== Üretim Planlama Programı ===")
    
    # İş ve makine sayılarını alıyoruz
    is_sayisi = int(input("Kaç iş var? "))
    makine_sayisi = int(input("Kaç makine var? "))
    print("-" * 40)

    # İşlem sürelerini alıyoruz
    islem_sureleri = []
    print("İşlem sürelerini giriniz:")
    for is_no in range(1, is_sayisi + 1):
        makine_sureleri = []
        for makine_no in range(1, makine_sayisi + 1):
            sure = int(input(f"İş {is_no} - Makine {makine_no} işlem süresi: "))
            makine_sureleri.append(sure)
        islem_sureleri.append(makine_sureleri)
    
    print("-" * 40)

    # Geçiş maliyetlerini alıyoruz
    gecis_maliyetleri = []
    print("Geçiş maliyetlerini giriniz:")
    for onceki_makine in range(1, makine_sayisi + 1):
        maliyetler = []
        for sonraki_makine in range(1, makine_sayisi + 1):
            maliyet = int(input(f"Makine {onceki_makine} -> Makine {sonraki_makine} geçiş maliyeti: "))
            maliyetler.append(maliyet)
        gecis_maliyetleri.append(maliyetler)

    print("-" * 40)

    # Girilen verileri ekrana yazıyoruz
    print("İşlem Süreleri Tablosu:")
    for is_no in range(is_sayisi):
        print(f"İş {is_no + 1}:", end=" ")
        for makine_no in range(makine_sayisi):
            print(f"Makine {makine_no + 1}: {islem_sureleri[is_no][makine_no]}", end=", ")
        print()
    
    print("\nGeçiş Maliyetleri Tablosu:")
    for onceki_makine in range(makine_sayisi):
        print(f"Makine {onceki_makine + 1} ->", end=" ")
        for sonraki_makine in range(makine_sayisi):
            print(f"Makine {sonraki_makine + 1}: {gecis_maliyetleri[onceki_makine][sonraki_makine]}", end=", ")
        print()
    print("-" * 40)

    # Dinamik programlama tabloları
    toplam_sure = [[float('inf')] * makine_sayisi for _ in range(is_sayisi)]
    onceki_makine_tablosu = [[-1] * makine_sayisi for _ in range(is_sayisi)]

    # İlk iş için sadece işlem süreleri yazılır
    for makine in range(makine_sayisi):
        toplam_sure[0][makine] = islem_sureleri[0][makine]

    # Diğer işler için en kısa süre hesaplanır
    for is_index in range(1, is_sayisi):
        for suanki_makine in range(makine_sayisi):
            for onceki_makine in range(makine_sayisi):
                hesaplanan_sure = (toplam_sure[is_index - 1][onceki_makine] +
                                   gecis_maliyetleri[onceki_makine][suanki_makine] +
                                   islem_sureleri[is_index][suanki_makine])
                if hesaplanan_sure < toplam_sure[is_index][suanki_makine]:
                    toplam_sure[is_index][suanki_makine] = hesaplanan_sure
                    onceki_makine_tablosu[is_index][suanki_makine] = onceki_makine

    # Minimum toplam süre ve son makine bulunur
    en_kisa_sure = min(toplam_sure[is_sayisi - 1])
    son_makine = toplam_sure[is_sayisi - 1].index(en_kisa_sure)

    # Hangi işin hangi makinede yapıldığı bulunur
    makine_secimi = [0] * is_sayisi
    makine_secimi[-1] = son_makine
    for is_index in range(is_sayisi - 1, 0, -1):
        makine_secimi[is_index - 1] = onceki_makine_tablosu[is_index][makine_secimi[is_index]]

    # Sonuçları yazdır
    print("\n🔵 Minimum Toplam Süre:", en_kisa_sure)
    print("\nİşlerin Sırası ve Kullanılan Makineler:")
    for is_no in range(is_sayisi):
        print(f"İş {is_no + 1}: Makine {makine_secimi[is_no] + 1}")

    # Geçişleri yazdır ve toplam geçiş maliyetini hesapla
    toplam_gecis_maliyeti = 0
    print("\nGeçişler:")
    for is_no in range(is_sayisi - 1):
        from_makine = makine_secimi[is_no]
        to_makine = makine_secimi[is_no + 1]
        gecis = gecis_maliyetleri[from_makine][to_makine]
        toplam_gecis_maliyeti += gecis
        print(f"Makine {from_makine + 1} -> Makine {to_makine + 1} (Maliyet: {gecis})")

    print("\n🟢 Toplam Geçiş Maliyeti:", toplam_gecis_maliyeti)
    print("-" * 40)

# Programı çalıştırmak için
if __name__ == "__main__":
    main()
