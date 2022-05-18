#İSVİÇRE SİSTEMİ SATRANÇ OYUNCUSU EŞLEŞTİRME KURALLARINA BENZER OLARAK EŞLEŞTİRME  YAPIP TURNUVA SONU NİHAİ SIRALAMA LİSTESİ VE ÇAPRAZ TABLO BASTIRAN PROGRAM.
#YASİN ÖZKURT-05190000087- ALGORİTMA VE PROGRAMLAMA DERSİ İLK DÖNEM FİNAL PROJESİ.
letters_dict ={" ":30,"A": 0, "B": 1, "C": 2, "Ç": 3, "D": 4, "E": 5, "F": 6, "G": 7, "Ğ": 8, "H": 9, "I": 10, "İ": 11,"J": 12, "K": 13,
               "L": 14, "M": 15, "N": 16, "O": 17, "Ö": 18, "P": 19, "R": 20, "S": 21, "Ş": 22,"T": 23, "U": 24, "Ü": 25, "V": 26, "Y":27,"Z":28}
#BU FONKSİYON İSTEDİĞİMİZ LİSTENİN İKİNCİ BOYUTUNDAKİ TÜRKÇE HARFLER DE İÇEREN STRİNGLERİ SIRALIYOR
def modifiye_bubbleSort(letters_dict,arr,k):  #adsoyad sıralamasında kullanılacak modifiye ettiğim bubble sort, k burada listenin ikinci boyutundaki aradığımız elemanın indexi
   n = len(arr)
   for i in range(n - 1):
      for j in range(0, n - i - 1):
         if ("ç" in arr[j][k] or "ğ" in arr[j][k] or "ö" in arr[j][k] or "ş" in arr[j][k] or "ü" in arr[j][k]) or (("ç" in arr[j+1][k] or "ğ" in arr[j+1][k] or "ö" in arr[j+1][k] or "ş" in arr[j+1][k] or "ü" in arr[j+1][k]) ):
            for x in range(len(min(arr[j][k],arr[j+1][k]))):
               if letters_dict[arr[j][k][x]] > letters_dict[arr[j+1][k][x]]:
                  arr[j], arr[j + 1] = arr[j + 1], arr[j]
                  break
               elif letters_dict[arr[j][k][x]] < letters_dict[arr[j+1][k][x]]:
                  break
         else:
            if arr[j][k] > arr[j + 1][k]:
               arr[j], arr[j + 1] = arr[j + 1], arr[j]
   return arr
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
def ilk_girdiler():
    tüm_oyuncuların_bilgileri_liste=[]
    toplam_oyuncu_sayısı=0
    # girdiler hata kontrolleri:
    x=True
    lno_kontrolü=[]
    while x:
        oyuncu_bilgileri = []
        l_no=int(input("Oyuncu lisans numarası giriniz(bitirmek için 0 ya da negatif bir sayı giriniz) : "))
        while type(l_no) == str : #hata kontrolü
            l_no = int(input("Lütfen bir sayı giriniz ! (bitirmek için 0 ya da negatif bir sayı giriniz) : "))
        while l_no in lno_kontrolü:
            l_no = int(input("Oyuncu lisans numarası giriniz(bitirmek için 0 ya da negatif bir sayı giriniz) : "))

        if l_no <=0:  #kullanıcının programı sonlandırmak istediği durum.
            x=False
        else:
            ad_soyad=input("Oyuncunun adini-soyadini giriniz:")
            if "i"  in  ad_soyad:
                ad_soyad=ad_soyad.replace("i","İ")
            ad_soyad=ad_soyad.upper()
            fide_elo=int(input("Oyuncunun ELO’sunu giriniz (en az 1000, yoksa 0)"))
            while   (fide_elo < 1000  and fide_elo != 0 ) : # hata kontrolü
                fide_elo = int(input("Lütfen oyuncunun ELO’sunu kriterlere uygun biçimde tekrar  giriniz (en az 1000, yoksa 0)"))
            ukd_elo = int(input("Oyuncunun UKD’sini giriniz (en az 1000, yoksa 0)"))
            while (ukd_elo < 1000 and ukd_elo != 0):  # hata kontrolü
                ukd_elo = int(input("Lütfen oyuncunun UKD’sini kriterlere uygun biçimde tekrar  giriniz (en az 1000, yoksa 0)"))
            oyuncu_bilgileri.append(l_no)    # bu bölmede daha sonra genel listeye eklenecek olan tek bir oyuncunun bilgilerini içeren geçici liste oluşturuluyor.
            oyuncu_bilgileri.append(ad_soyad)
            oyuncu_bilgileri.append(ukd_elo)
            oyuncu_bilgileri.append(fide_elo)
            oyuncu_bilgileri.append(0) #henüz puanlar 0 olduğu için böyle ekledim
            lno_kontrolü.append(l_no)
            # Bir de daha sonraki fonksiyonlardan birinde  bu listeye başlangıç sıra numaraları ekleniyor .
            toplam_oyuncu_sayısı+=1
            tüm_oyuncuların_bilgileri_liste.append(oyuncu_bilgileri)  # burada genel listeye tek bir oyuncunun bilgilerini ekledik.
    return tüm_oyuncuların_bilgileri_liste,toplam_oyuncu_sayısı
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
def sıralayıcı(tüm_oyuncuların_bilgileri_liste,toplam_oyuncu_sayısı):
    # Oyuncular farklı etkenlerin önem sırasına göre sıralanıyor ve  iki boyutlu'tüm_oyuncuların_bilgileri_liste' içinde tutuluyor.
    tüm_oyuncuların_bilgileri_liste.sort( key=lambda oyuncu_bilgileri: oyuncu_bilgileri[0])  # en önemsiz kriter  lisans no.
    modifiye_bubbleSort(letters_dict,tüm_oyuncuların_bilgileri_liste,1)  # kriter ad soyad alfabetik sıralama
    tüm_oyuncuların_bilgileri_liste.sort(reverse=True,key=lambda oyuncu_bilgileri: oyuncu_bilgileri[2])  # kriter ukd elo
    tüm_oyuncuların_bilgileri_liste.sort(reverse=True,key=lambda oyuncu_bilgileri: oyuncu_bilgileri[3])  # kriter fide elo.
    tüm_oyuncuların_bilgileri_liste.sort(reverse=True,key=lambda oyuncu_bilgileri: oyuncu_bilgileri[4])  # en önemli kriter puan
    return tüm_oyuncuların_bilgileri_liste,toplam_oyuncu_sayısı
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
def başlangıç_sıralama_yazdır(tüm_oyuncuların_bilgileri_liste,toplam_oyuncu_sayısı):
    eşleşmeler_dict = {}
    renkler_dict={}
    mac_sonucları_dict={}
    puanlar_dict= {}
    semboller_dict={}
    print("Başlangıç Sıralama Listesi  ")
    print("BSNo    LNo      Ad-Soyad     Elo    Ukd")
    print("----   ----    ------------   ----   ----")
    for i in range(toplam_oyuncu_sayısı):
        BSNo=i+1  # sabit değişken
        tüm_oyuncuların_bilgileri_liste[i].append(BSNo) # oyuncu bilgilerini içeren sıralı listeye her oyuncu için bir başlangıç sıra numarası ekledim.
        print(format(BSNo,"4d"),end="   ")              #listenin son durumu sırayla [[lno,adsoyad,ukd-elo,fide-elo,puan,bsno],[..],...].
        print(format(tüm_oyuncuların_bilgileri_liste[i][0],"4d"),end="    ")
        boşluk_stringi=(15-int(len(tüm_oyuncuların_bilgileri_liste[i][1])))*" "
        print(tüm_oyuncuların_bilgileri_liste[i][1],end=boşluk_stringi)
        print(format(tüm_oyuncuların_bilgileri_liste[i][3],"4d" ),end="   ")
        print(format(tüm_oyuncuların_bilgileri_liste[i][2],"4d"))

        eşleşmeler_dict[BSNo]=[]  #başlangıç sıra no'yu her oyuncuya ait değişmez işaret olarak kullanıyorum ,  bu sözlük eşleştirici fonksiyonda kullanılacak.
        renkler_dict[BSNo]=[]
        mac_sonucları_dict[BSNo]=[]
        puanlar_dict[BSNo]=[]
        semboller_dict[BSNo]=[]
    return eşleşmeler_dict,renkler_dict,mac_sonucları_dict,puanlar_dict,semboller_dict
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
kontrol_listesi=[0] #BU LİSTE EŞLEŞTİR VE YAZDIR FONKSİYONUNU İLK TUR VE SONRASI OLARAK İKİYE BÖLMEDE KULLANILIYOR.
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
def eşleştir_ve_yazdır(eşleşmeler_dict,renkler_dict,toplam_oyuncu_sayısı,tüm_oyuncuların_bilgileri_liste,kontrol_listesi,ilk_oyuncu_ilk_renk,ikinci_oyuncu_ilk_renk,tur,rakibi_gelmeyip_tur_atlayanlar_listesi,mac_sonucları_dict,semboller_dict):
    # ----------------İLK KISIMDA SADECE İLK EŞLEŞME İÇİN YAZILAN KOD ÇALIŞIYOR--------------------
    if len(kontrol_listesi)==1: #bu ilk eşleşme için bu parçanın bir defa çalışması için.
        kontrol_listesi.append(2)
        #BURADA RENKLERİ KAYDEDİYORUZ
        eşleşme_sıralı_list = tüm_oyuncuların_bilgileri_liste.copy()
        if toplam_oyuncu_sayısı % 2 == 0:  # EĞER ÇİFT SAYIDA OYUNCU VARSA
            i = 1
            while i < toplam_oyuncu_sayısı:
                renkler_dict[i] = [ilk_oyuncu_ilk_renk]
                renkler_dict[i + 1] = [ikinci_oyuncu_ilk_renk]  # İlk verilen renklere göre renkler sözlüğüne BSNolara göre oyuncuların ilk maç aldığı renkler kaydediliyor
                i += 2
        else:
            bsno = 1
            for x in range(int(toplam_oyuncu_sayısı / 2)):
                renkler_dict[bsno] = [ilk_oyuncu_ilk_renk]
                renkler_dict[bsno + 1] = [ikinci_oyuncu_ilk_renk]
                bsno += 2
            eşleşme_sıralı_list.remove(eşleşme_sıralı_list[-1])
            renkler_dict[toplam_oyuncu_sayısı] = ["BYE"] #İlk tur için son oyuncu bye atanıyor
        #---------------------------------------------------------------
        #BURADA EŞLEŞME SÖZLÜĞÜNE İLK EŞLEŞMENİN KEYLERİ YAZILIYOR.
        i = 1
        while i < toplam_oyuncu_sayısı:
            eşleşmeler_dict[i] = [i + 1]  # tutulan keyler= 1,3,5,7
            i += 2

        j = 2
        while j < toplam_oyuncu_sayısı:
            eşleşmeler_dict[j] = [j - 1]  # BURADA İLK EŞLEŞMELER EŞLEŞME SÖZLÜĞÜNDE TUTULDU
            j += 2
        if toplam_oyuncu_sayısı % 2 ==0:
            eşleşmeler_dict[toplam_oyuncu_sayısı]=[toplam_oyuncu_sayısı-1]
        if toplam_oyuncu_sayısı % 2 != 0:
            eşleşmeler_dict[toplam_oyuncu_sayısı] += ["BYE"]
            mac_sonucları_dict[toplam_oyuncu_sayısı] += [1]
            semboller_dict[toplam_oyuncu_sayısı]+=[1]
        #--------DAHA SONRA İLK EŞLEŞME YAZDIRILIYOR---------------------
        eşleşme_sıralı_list_yeni = []  # BURADA EŞLEŞME LİSTESİNİN RENKLERİNİ BS BS BS ŞEKLİNDE DİZDİK Kİ PRİNT EDERKEN İŞİMİZ KOLAYLAŞSIN
        for i in range(0, len(eşleşme_sıralı_list), 2):
            if renkler_dict[eşleşme_sıralı_list[i][5]][-1] == "B":
                eşleşme_sıralı_list_yeni.append(eşleşme_sıralı_list[i])
                eşleşme_sıralı_list_yeni.append(eşleşme_sıralı_list[i + 1])
            else:
                eşleşme_sıralı_list_yeni.append(eşleşme_sıralı_list[i + 1])
                eşleşme_sıralı_list_yeni.append(eşleşme_sıralı_list[i])
        print("          Beyazlar             Siyahlar")
        print("MNo   BSNo   LNo   Puan - Puan   LNo   BSNo")
        print("---   ----   ---   ----   ----   ---   ----")
        MNo = 1
        for i in range(0, len(eşleşme_sıralı_list_yeni), 2):
            print(format(MNo, "3d"), end="   ")  # Masa no
            print(format(eşleşme_sıralı_list_yeni[i][5], "4d"), end="   ")  # BSNo
            print(format(eşleşme_sıralı_list_yeni[i][0], "3d"), end="   ")  # lno
            print(format(eşleşme_sıralı_list_yeni[i][4], "4g"), end="   ")  # Puan
            print(format(eşleşme_sıralı_list_yeni[i + 1][4], "4g"), end="   ")  # Puan
            print(format(eşleşme_sıralı_list_yeni[i + 1][0], "3d"), end="   ")  # lno
            print(format(eşleşme_sıralı_list_yeni[i + 1][5], "4d"))  # BSNo
            MNo += 1
        if toplam_oyuncu_sayısı % 2 == 1:  # TEK SAYID OYUNCU VARSA ELBET BİRİLERİ BYE OLACAĞINDAN BU SEKMEYE GİRİYOR.
            for i in range(toplam_oyuncu_sayısı):  # BURADA BYE ATANAN OYUNCUYU BULUP EŞLEŞME LİSTESİNİN SONUNA YAZDIRIYORUZ.
                if eşleşmeler_dict[tüm_oyuncuların_bilgileri_liste[i][5]][-1] == "BYE":
                    BYE_atanan_eleman_bilgileri = tüm_oyuncuların_bilgileri_liste[i]
            print(format(MNo, "3d"), end="   ")  # Masa no
            print(format(BYE_atanan_eleman_bilgileri[5], "4d"), end="   ")  # BSNo
            print(format(BYE_atanan_eleman_bilgileri[0], "3d"), end="   ")  # lno
            print(format(BYE_atanan_eleman_bilgileri[4], "4g"), end="   ")  # Puan
            print("      BYE")
        kontrol_listesi.append(1)  # ilk eşleme için yazılan farklı 2 kod parçasının tekrar  çalışmaması için .
        kontrol_listesi.append(2)

        return eşleşme_sıralı_list_yeni,eşleşmeler_dict
    #----------------------------------------------------------------------------------------
    else:   #BURADA İSE İLK SEFER HARİCİNDEKİ EŞLEŞME ALGORİTMASI ÇALIŞIYOR.
        tüm_oyuncuların_bilgileri_liste2=tüm_oyuncuların_bilgileri_liste.copy()  # tüm oyuncuları bilgileri listesinde yapılacak değişikliklerden fonksiyonun dışındaki asıl liste etklenmesin diye kopyaladık.

        #RENKLERİ ÖNCEDEN DEĞİŞTİRİYORUM BYE ATAMASINI DA ÖNCEDEN YAPIYORUM
        def renk_değiştir(tüm_oyuncuların_bilgileri_liste, eşleşmeler_dict, renkler_dict,rakibi_gelmeyip_tur_atlayanlar_listesi):
            if len(tüm_oyuncuların_bilgileri_liste) % 2 == 1: #TEK SAYIDA OYUNCU VARSA BYE ATAMASI YAPILIYOR
                b = "NONE"
                i = 1
                while b != "BYE":
                    sonuncu_index = len(tüm_oyuncuların_bilgileri_liste) - i
                    BSNo_index = tüm_oyuncuların_bilgileri_liste[sonuncu_index][5]  # BSNo indexi
                    a = list(eşleşmeler_dict[BSNo_index])
                    if a[-1] != "BYE"  and (BSNo_index not in rakibi_gelmeyip_tur_atlayanlar_listesi) and "BYE" not in eşleşmeler_dict[BSNo_index]:
                        eşleşmeler_dict[BSNo_index] += ["BYE"]
                        renkler_dict[BSNo_index] += ["BYE"]
                        mac_sonucları_dict[BSNo_index]+=[1]
                        semboller_dict[BSNo_index]+=[1]
                        tüm_oyuncuların_bilgileri_liste2.remove(tüm_oyuncuların_bilgileri_liste[sonuncu_index]) # BU BYE ATANAN OYUNCUNUN EŞLEŞMEYE KATILMAMASI İÇİN
                        b = "BYE"
                    else:
                        i += 1
                for eleman in tüm_oyuncuların_bilgileri_liste2:  # İLK RENK ATAMA YANİ SÖZLÜKLERE YERLEŞTİRME FONKSİYON DIŞINDA YAPILDIĞINDAN BURADA OTOMATİK BAŞLIYOR.
                    x=eleman[5]
                    if renkler_dict[x ][-1] == "B":
                        renkler_dict[x ] += ["S"]
                    elif renkler_dict[x ][-1] == "S":
                        renkler_dict[x ] += ["B"]
            else: #OYUNCU SAYISI ÇİFT İSE KİMSE BYE GEÇMEYECEĞİNDEN DİREKT OLARAK RENKLER ZITTINA ÇEVİRİLİYOR-İLERİDE GEREKİRSE TEKRAR DEĞİŞTİRİLİYOR(EŞLEŞTİRME KISMINDA)
                for eleman in tüm_oyuncuların_bilgileri_liste:  # İLK RENK ATAMA YANİ SÖZLÜKLERE YERLEŞTİRME FONKSİYON DIŞINDA YAPILDIĞINDAN BURADA OTOMATİK BAŞLIYOR.
                    x=eleman[5]
                    if renkler_dict[x ][-1] == "B":
                        renkler_dict[x ] += ["S"]
                    else:
                        renkler_dict[x ] += ["B"]

        renk_değiştir(tüm_oyuncuların_bilgileri_liste, eşleşmeler_dict, renkler_dict,rakibi_gelmeyip_tur_atlayanlar_listesi) #RENK DEĞİŞTİRME FONKSİYONUNU ÇAĞIRIYORUZ
        #BU FONKSİYON EŞLEŞTİRME KISMINDA OYUNCULARIN ÖNCEKİ RENKLERİNİ KONTROL ETMEMİZİ SAĞLIYOR.
        def üst_üste_aynı_renk_mi_geldi(renkler_dict, BSNo):  # BU FONK ÜST ÜSTE AYNI RENK GELDİYSE FALSE, GELMEDİYSE TRUE DÖNÜYOR
           kullanılmış=0
           if len(renkler_dict[BSNo])==1 or len(renkler_dict[BSNo])==2:
               return True
           else:
               for i in range(1,3):
                   if renkler_dict[BSNo][-i-1]== zıt_renk_bulucu(renkler_dict[BSNo][-1]):
                       kullanılmış+=1
               if kullanılmış>=2:
                   return False
               else:
                   return True

        #BU FONKSİYON ONA VERDİĞİMİZ RENGİN TERSİNİ BİZE VERİYOR.BUNU DA EŞLEŞTİRME KISMINDA KULLANIYORUM.
        def zıt_renk_bulucu(renk):
            if renk == "B":
                renk = "S"
            else:
                renk = "B"
            return renk
        #-------------------!!!EŞLEŞTİRME ALGORİTMASI!!!---------------------------------

        eşleşme_sıralı_list=[]#Bu listeye eşleşen oyuncular sırayla kaydedilecek
        for i in range(int(toplam_oyuncu_sayısı / 2)):  # YAPILACAK EŞLEŞME SAYISI  KADAR DÖNÜYOR
            artış = 0
            eşleşti = False
            rao = tüm_oyuncuların_bilgileri_liste2[0]  # RAKİP ARANAN OYUNCU(RAO) RAKİP ARANACAK LİSTEDEN ÇIKARILIYOR
            tüm_oyuncuların_bilgileri_liste2.pop(0)  # raoyu listeden çıkarıyorum.
            eşleşti2 = False
            while eşleşti == False:  # BİR EŞLEŞME YAPILINCAYA KADAR DÖNECEK
                aşağı_indik = False #BU VE HEMEN ALTINDAKİ BİZE 1 2 VE 3. SEKMELER ARASINDA 3E GİREN OLURSA(BEST CASE) 2 VE 1İ ,2YE GİREN OLURSA 1İ BOŞVERMEMİZİ SAĞLIYOR
                aşağı_indik2 = False
                geçici_liste = []#BU RAKİP ARANAN OYUNCUNUN EŞİT YA DA EN YAKIN PUAN DÜZEYİNDEKİ RAKİPLERİNİ TUTUYOR.
                atandı = 0
                nerede_eşleşti = 0
                bu_tur_atama_yapıldı=0


                for i in range(len(tüm_oyuncuların_bilgileri_liste2)):  # RAO İLE İSTENEN PUANA SAHİP RAKİPLER TUTULDU
                    if (tüm_oyuncuların_bilgileri_liste2[i] not in eşleşme_sıralı_list) and  tüm_oyuncuların_bilgileri_liste2[i][5] not in eşleşmeler_dict[rao[5]]:  # bu da daha önceden eşleşmiş olma ihtimali için önlem
                        if rao[4] == tüm_oyuncuların_bilgileri_liste2[i][4] + artış:
                            geçici_liste += [tüm_oyuncuların_bilgileri_liste2[i]]
                for i in range(len(geçici_liste)):
                    if (renkler_dict[rao[5]][-1] == renkler_dict[geçici_liste[i][5]][-1] or  renkler_dict[rao[5]][-1]=="BYE" )   and (üst_üste_aynı_renk_mi_geldi(renkler_dict, rao[5])) and (aşağı_indik == False):  # BU 3 SEKME YUKARIDA BAHSETTİĞİMİZ GİBİ RENK KARŞILAŞTIRMASI YAPIYOR.
                        eşleşti2 = True
                        nerede_eşleşti = 1
                        hangi_index_eşleşti = i#****
                        bu_tur_atama_yapıldı+=1

                    if (renkler_dict[rao[5]][-1] == renkler_dict[geçici_liste[i][5]][-1]  or   renkler_dict[geçici_liste[i][5]][-1] =="BYE")    and üst_üste_aynı_renk_mi_geldi(renkler_dict, geçici_liste[i][5]) and aşağı_indik2 == False:
                        aşağı_indik = True  # Tekrar yukarıda eşleştirilmemesi için.
                        nerede_eşleşti = 2
                        hangi_index_eşleşti = i
                        bu_tur_atama_yapıldı+1
                        eşleşti2 = True
                        aşağı_indik2 = True

                    if (renkler_dict[rao[5]][-1] != renkler_dict[geçici_liste[i][5]][-1])  or renkler_dict[rao[5]][-1]=="BYE" or renkler_dict[geçici_liste[i][5]][-1] =="BYE" :
                        eşleşti = True
                        eşleşti2 = True
                        nerede_eşleşti = 3
                        hangi_index_eşleşti=i
                        if renkler_dict[rao[5]][-1]=="BYE":
                            renkler_dict[rao[5]]+=[zıt_renk_bulucu(renkler_dict[geçici_liste[i][5]][-1])]
                        elif renkler_dict[geçici_liste[i][5]][-1]=="BYE":
                            renkler_dict[geçici_liste[i][5]]+=[zıt_renk_bulucu(renkler_dict[rao[5]][-1])]
                        break  # BU SEKMEDEKİ EŞLEŞME(KRİTERLERE GÖRE İLK SIRADAKİ) OLURSA DİREKT FOR DÖNGÜSÜ İÇİNDEN ÇIKMAK ZAMAN KAZANDIRIR
                if eşleşti2 == True:  # herhangi bir eşleşme yapıldıysa
                    eşleşti = True
                    # BURAYA EŞLEŞTİYSE NEREDE EŞLEŞTİĞİNİ BULUP O SEKMEYE ÖZEL RENK ATAMALARINI YAPAN KOD  YAZILACAK.
                    if nerede_eşleşti == 1:
                        if renkler_dict[rao[5]][-1]=="BYE":
                            renkler_dict[rao[5]] += [zıt_renk_bulucu([geçici_liste[hangi_index_eşleşti][5]][-1])]
                        else:
                            # BURADA İKİ OYUNCU RENKLERİNİN EŞİT OLDUĞUNU AMA 1. OYUNCUNUN RENGİNİN DEĞİŞEBİLİCEĞİ DURUM SÖZ KONUSU, DOLAYISIYLA BU BLOK İÇİNE GİRERSE 1. OYUNCUNUN RENGİNİN DEĞİŞMESİ GEREK
                            renkler_dict[rao[5]][-1] = zıt_renk_bulucu(renkler_dict[rao[5]][-1])
                            i = hangi_index_eşleşti

                    elif nerede_eşleşti == 2:
                        if renkler_dict[geçici_liste[hangi_index_eşleşti][5]][-1] =="BYE":
                            renkler_dict[geçici_liste[i][5]] += [zıt_renk_bulucu(renkler_dict[rao[5]][-1])]

                        # BURADA İKİ OYUNCU RENKLERİNİN EŞİT OLDUĞUNU AMA 2. OYUNCUNUN RENGİNİN DEĞİŞEBİLİCEĞİ DURUM SÖZ KONUSU, DOLAYISIYLA BU BLOK İÇİNE GİRERSE 2. OYUNCUNUN RENGİNİN DEĞİŞMESİ GEREK
                        i = hangi_index_eşleşti
                        renkler_dict[geçici_liste[i][5]][-1] = zıt_renk_bulucu(renkler_dict[geçici_liste[i][5]][-1])

                    #GEÇİCİ LİSTEDEKİ TÜM ELEMANLAR DÖNDÜKTEN SONRA EĞER EŞLEŞME VARSA BURAYA(yukarıdaki if eşleşti2==True bloğu) GİRİYOR.
                    #EN SON HANGİ GEÇİCİLİSTE ELEMANININ EŞLEŞTİĞİ HANGİ_İNDEX_EŞLEŞTİ SABİTİNDE TUTULUYOR
                    #BİZ DE HANGİ ELEMANIN EŞLEŞTİĞİNİ EN SON BURADA ÖĞRENİP DİCTE VE LİSTEYE ATIYORUZ.
                    #ATAMALAR KISMI:
                    #***************************************************************************************************
                    eşleşmeler_dict[rao[5]] += [geçici_liste[hangi_index_eşleşti][5]]  # BURADA TARAFLARI EŞLEŞTİRME SÖZLÜĞÜNE KAYDEDİYORUZ VE BİR LİSTEYE EKLİYORUZ
                    eşleşmeler_dict[geçici_liste[hangi_index_eşleşti][5]] += [rao[5]]
                    eşleşme_sıralı_list.append(rao)
                    eşleşme_sıralı_list.append(geçici_liste[hangi_index_eşleşti])
                    tüm_oyuncuların_bilgileri_liste2.remove(geçici_liste[hangi_index_eşleşti])  # EŞLEŞEN RAKİP OYUNCUYU LİSTEDEN ÇIKARDIM
                    #***************************************************************************************************
                else:
                    artış += 0.5
                    eşleşti = False  # BURADA İSE GEÇİCİ LİSTEDEKİ HER ELEMANI DÖNÜDRMÜŞ ANCAK EŞLEMEMİŞSE YENİ BİR GEÇİCİ LİSTE YAPMASI İÇİN PUANI 0.5 ARTIRIP GERİ YOLLUYORUZ.
        # --------------EŞLEŞTİRME ALGO SON KISMI--------------------------------------------------
        eşleşme_sıralı_list_yeni = []  # BURADA EŞLEŞME LİSTESİNİN RENKLERİNİ BS BS BS ŞEKLİNDE DİZDİK
        for i in range(0, len(eşleşme_sıralı_list), 2):
            if renkler_dict[eşleşme_sıralı_list[i][5]][-1] == "B":
                eşleşme_sıralı_list_yeni.append(eşleşme_sıralı_list[i])
                eşleşme_sıralı_list_yeni.append(eşleşme_sıralı_list[i + 1])
            else:
                eşleşme_sıralı_list_yeni.append(eşleşme_sıralı_list[i + 1])
                eşleşme_sıralı_list_yeni.append(eşleşme_sıralı_list[i])
        # ----------------------------------------------------------------
        print(f"{tur+1}. Tur Eşleştirme Listesi")
        print("          Beyazlar             Siyahlar")
        print("MNo   BSNo   LNo   Puan - Puan   LNo   BSNo")
        print("---   ----   ---   ----   ----   ---   ----")
        MNo = 1
        for i in range(0, len(eşleşme_sıralı_list_yeni), 2):
            print(format(MNo, "3d"), end="   ")  # Masa no
            print(format(eşleşme_sıralı_list_yeni[i][5], "4d"), end="   ")  # BSNo
            print(format(eşleşme_sıralı_list_yeni[i][0], "3d"), end="   ")  # lno
            print(format(eşleşme_sıralı_list_yeni[i][4], "4g"), end="   ")  # Puan
            print(format(eşleşme_sıralı_list_yeni[i + 1][4], "4g"), end="   ")  # Puan
            print(format(eşleşme_sıralı_list_yeni[i + 1][0], "3d"), end="   ")  # lno
            print(format(eşleşme_sıralı_list_yeni[i + 1][5], "4d"))  # BSNo
            MNo += 1
        if toplam_oyuncu_sayısı % 2 ==1: #TEK SAYID OYUNCU VARSA ELBET BİRİLERİ BYE OLACAĞINDAN BU SEKMEYE GİRİYOR.
            for i in range(toplam_oyuncu_sayısı):  # BURADA BYE ATANAN OYUNCUYU BULUP EŞLEŞME LİSTESİNİN SONUNA YAZDIRIYORUZ.
                if eşleşmeler_dict[tüm_oyuncuların_bilgileri_liste[i][5]][-1] == "BYE":
                    BYE_atanan_eleman_bilgileri = tüm_oyuncuların_bilgileri_liste[i]
                    bsno=BYE_atanan_eleman_bilgileri[5]
            print(format(MNo, "3d"), end="   ")  # Masa no
            print(format(BYE_atanan_eleman_bilgileri[5], "4d"), end="   ")  # BSNo
            print(format(BYE_atanan_eleman_bilgileri[0], "3d"), end="   ")  # lno
            print(format(BYE_atanan_eleman_bilgileri[4], "4g"), end="   ")  # Puan
            print("      BYE")

        return eşleşme_sıralı_list_yeni, eşleşmeler_dict
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
def mac_sonucu_çözümleyici(mac_sonucu): #ÖNCE MAÇ SONUCU SONRA SEMBOL RETURN EDİLİYOR.
        if mac_sonucu==0:
            return 0.5,0.5,chr(189),chr(189) #mac sonucu kodunu puana dönüştürüyor
        elif mac_sonucu==1:
            return 1,0,"1","0"
        elif mac_sonucu==2:
            return 0,1,"0","1"
        elif mac_sonucu==3:
            return 1,0,"+","-"
        elif mac_sonucu==4:
            return 0,1,"-","+"
        else:
            return 0,0,"-","-"
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
def parti_sonuc_alıcı(toplam_oyuncu_sayısı,kaçıncı_tur,tüm_oyuncuların_bilgileri_liste,eşleşme_sırası_list,puanlar_dict,renkler_dict,eşleşmeler_dict,rakibi_gelmeyip_tur_atlayanlar_listesi,semboller_dict,mac_sonucları_dict):
    #PARTİ SONUCU PUANLARI ASIL LİSTEYE(SIRALAMA YAPILAN , EŞLEŞTİRİLMEDE KULLANILAN GENEL OYUNCU BİLGİLERİ LİSTESİ) EKLENMELİ.
    for i in range(toplam_oyuncu_sayısı):
        puanlar_dict[i+1]=[]  #BURADA HER BSNO İÇİN PUANLARIN TUTULACAĞI BİR DİCT HAZIRLANDI.HER DÖÜNŞTE SIFILANIYOR,ZATEN İŞLEVİ GENEL LİSTEYE PUANLARI AKTARMAK
    MASA_SAYISI=int(toplam_oyuncu_sayısı/2)
    sırayla_oyuncu_puanları=[]
    if renkler_dict[eşleşme_sırası_list[0][5]][-1] == "B":
        x=0
        for i in range(MASA_SAYISI):
            mac_sonucu=int(input(f"{kaçıncı_tur}. turda {i+1}. masada oynanan maçın sonucunu giriniz (0-5) :"))
            while mac_sonucu not in [0,1,2,3,4,5]:
                mac_sonucu = int(input(f"{kaçıncı_tur}. turda {i + 1}. masada oynanan maçın sonucunu giriniz (0-5) :"))
            if mac_sonucu == 3:
                rakibi_gelmeyip_tur_atlayanlar_listesi.append(eşleşme_sırası_list[x][5])#BEYAZ RENKLİ BEDAVADAN TUR ATLAYAN ELEMANI EKLEDİK
            elif mac_sonucu == 4 :
                rakibi_gelmeyip_tur_atlayanlar_listesi.append(eşleşme_sırası_list[x+1][5])#BEYAZ RENKLİ BEDAVADAN TUR ATLAYAN ELEMANI EKLEDİK

            oyuncu_puan1,oyuncu_puan2,gösterim1,gösterim2=mac_sonucu_çözümleyici(mac_sonucu) #BEYAZ SİYAH ŞEKLİNDE PUANLAR GELİYOR.
            sırayla_oyuncu_puanları.append(oyuncu_puan1)
            sırayla_oyuncu_puanları.append(oyuncu_puan2)
            semboller_dict[eşleşme_sırası_list[x][5]].append(gösterim1)
            semboller_dict[eşleşme_sırası_list[x+1][5]].append(gösterim2)
            mac_sonucları_dict[eşleşme_sırası_list[x][5]].append(oyuncu_puan1)
            mac_sonucları_dict[eşleşme_sırası_list[x + 1][5]].append(oyuncu_puan2)
            x+=2
    if toplam_oyuncu_sayısı % 2==1:
        sırayla_oyuncu_puanları.append(1)  #BYE YERİNE 1 ATADIK ÇÜNKÜ BYE GEÇEN ELEMAN 1 PUAN ALMIŞ BİÇİMDE GEÇİYOR
    sıra=0
    for i in range(len(eşleşme_sırası_list)):#EŞLEŞME LİSTESİNDE SIRAYLA BSNOLAR DÖNECEK
        BSNo=eşleşme_sırası_list[i][5]
        puanlar_dict[BSNo]+=[sırayla_oyuncu_puanları[sıra]] #puanlar sözlüğüne oyuncuların aldığı puanları atadık
        sıra+=1
    for i in range(toplam_oyuncu_sayısı):#o tur varsa bye geçenin bsnosunu buluyoruz
        if eşleşmeler_dict[i+1][-1]=="BYE":
            Bye_geçen_Bsno=i+1
    if toplam_oyuncu_sayısı % 2 ==1: #BURADA BU TUR BYE GEÇEN ELEMANIN PUANINI PUANLAR SÖZLÜĞÜNE EKLİYORUZ
        puanlar_dict[Bye_geçen_Bsno]+=[1]
    for i in range(toplam_oyuncu_sayısı):
        tüm_oyuncuların_bilgileri_liste[i][4]+=puanlar_dict[tüm_oyuncuların_bilgileri_liste[i][5]][-1] #BURADA DA TÜM OYUNCU BİLGİLERİ LİSTESİNE OYUNCULARIN ALDIKLARI PUANLAR EKLENİYOR
    return tüm_oyuncuların_bilgileri_liste,rakibi_gelmeyip_tur_atlayanlar_listesi
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
def bh1_bh2(mac_sonucları_dict,semboller_dict,tüm_oyuncuların_bilgileri_liste,tur_sayısı,eşleşmeler_dict,en_sonki_liste):
    def bu_bsno_genel_bilgileri(BSNo,tüm_oyuncuların_bilgileri_liste):#BU FONK BSNOSUNU VERDİĞİMİZ OYUNCUNUN TÜM BİLGİLERİNİ LİSTE OLARAK DÖNÜYOR.
        for i in range(len(tüm_oyuncuların_bilgileri_liste)):
            if tüm_oyuncuların_bilgileri_liste[i][5]==BSNo:
                return tüm_oyuncuların_bilgileri_liste[i]
    bsnoyagöre_puanlar={}
    for eleman in tüm_oyuncuların_bilgileri_liste:
        bsnoyagöre_puanlar[eleman[5]]=eleman[4] #BSNOYA GÖRE PUANLAR SÖZLÜĞÜNDE HER BSNONUN ALDIĞI TOPLAM PUAN TUTULDU
    #*******************************************************************************************************************
    for i in range(len(tüm_oyuncuların_bilgileri_liste)):#her oyuncu için dönecek bize i+1 bsnolu oyuncunun bilgileri verecek
    #---------------------------------------------------------------
        bu_oyuncunun_eşleşme_listesi=eşleşmeler_dict[i+1]
        bu_oyuncunun_maç_sonuçları_listesi=mac_sonucları_dict[i+1]
        bu_oyuncunun_sembol_listesi=semboller_dict[i+1]
    #------------------------------------------------
        toplam_puan=0
        kaç_tur=len(bu_oyuncunun_eşleşme_listesi)
        puanlar_listesi=[]
        for x in range(len(bu_oyuncunun_eşleşme_listesi)):#herhangi bir liste aynı uzunluğa sahip olacağından seçtiğimiz farketmez.BURADA X KAÇINCI TURDA OLDUĞUMUZU BELİRTİYOR
            if bu_oyuncunun_eşleşme_listesi[x]== "BYE":
                buradan_çıkan_puan=sum(bu_oyuncunun_maç_sonuçları_listesi[0:x])+((kaç_tur-(x+1))*0.5)
                puanlar_listesi.append(buradan_çıkan_puan)
            else:
                if bu_oyuncunun_sembol_listesi[x]=="+"  :#RAKİBİN GELMEMESİ DURUMU
                    buradan_çıkan_puan=sum(bu_oyuncunun_maç_sonuçları_listesi[0:x])+((kaç_tur-(x+1))*0.5)
                    puanlar_listesi.append(buradan_çıkan_puan)
                elif bu_oyuncunun_sembol_listesi[x]=="-":# KENDİ GİTMEMİŞ
                    buradan_çıkan_puan = sum(bu_oyuncunun_maç_sonuçları_listesi[0:x]) + ((kaç_tur - (x + 1)) * 0.5)
                    puanlar_listesi.append(buradan_çıkan_puan)
                else:
                    buradan_çıkan_puan=bu_bsno_genel_bilgileri(eşleşmeler_dict[i+1][x],tüm_oyuncuların_bilgileri_liste)[4]
                    puanlar_listesi.append(buradan_çıkan_puan)
        sıralı_puanlar_listesi=sorted(puanlar_listesi)#BH1 için:
        sıralı_puanlar_listesi.pop(0)
        toplam_puan=sum(sıralı_puanlar_listesi)
        sıralı_puanlar_listesi2 = sorted(puanlar_listesi)#BH2 için:
        sıralı_puanlar_listesi2.pop(0)
        sıralı_puanlar_listesi2.pop(0)
        toplam_puan2=sum(sıralı_puanlar_listesi2)
    #BURADA ELEMANLARA BH1 PUANLARINI EKLİYORUZ
        for index in range(len(en_sonki_liste)):
            if en_sonki_liste[index][5]==i+1:
                en_sonki_liste[index].append(toplam_puan) #böylece genel bilgiler listesinde bsnodan sonra 6. index olarak BH1 değeri tutuldu.
                en_sonki_liste[index].append(toplam_puan2)#burada da bh2ler 7.index olarak tutuldu

    return en_sonki_liste
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
def sonneborn(tüm_oyuncuların_bilgileri_liste,eşleşmeler_dict,mac_sonucları_dict,semboller_dict,en_sonki_liste):
    kaç_tur=len(eşleşmeler_dict[1]) #en az bir oyuncu olacağından tur sayısını böyle bulabiliriz.
    for i in range(len(tüm_oyuncuların_bilgileri_liste)):#her oyuncu için dönecek
        toplam_puan=0
        bu_oyuncunun_eşleşme_listesi = eşleşmeler_dict[i + 1]
        bu_oyuncunun_maç_sonuçları_listesi = mac_sonucları_dict[i + 1]
        bu_oyuncunun_sembol_listesi = semboller_dict[i + 1]
        for j in range(len(semboller_dict[i+1])):#eşleşme sayısı kadar dönecek
            if eşleşmeler_dict[i+1][j]=="BYE":
                buradan_çıkan_puan=((kaç_tur-(j+1))*0.5)+sum(bu_oyuncunun_maç_sonuçları_listesi[0:j])
                toplam_puan+=buradan_çıkan_puan
            else:
                if semboller_dict[i+1][j]=="+" :#RAKİBİN GELMEMESİ DURUMU
                    buradan_çıkan_puan = ((kaç_tur - (j + 1)) * 0.5) + sum(bu_oyuncunun_maç_sonuçları_listesi[0:j])
                    toplam_puan += buradan_çıkan_puan
                elif   semboller_dict[i+1][j]==chr(189):#BERABERE KALINAN DURUM
                    rakip_bsno=eşleşmeler_dict[i+1][j]
                    buradan_çıkan_puan=sum(mac_sonucları_dict[rakip_bsno])/2 #YENDİĞİ YA DA BERABERE KALDDIĞI RAKİPLERİN PUANLARI TOPLAMININ YARISI
                    toplam_puan+=buradan_çıkan_puan
                elif semboller_dict[i+1][j]=="1":#YENDİĞİ DURUM
                    rakip_bsno = eşleşmeler_dict[i + 1][j]
                    buradan_çıkan_puan=sum(mac_sonucları_dict[rakip_bsno])
                    toplam_puan+=buradan_çıkan_puan
        for index in range(len(en_sonki_liste)):
            if en_sonki_liste[index][5] == i + 1:
                en_sonki_liste[index].append(toplam_puan)  # böylece genel bilgiler listesinde bh1 ve bh2den sonra 8. index olarak Sonneborn Berger( SB) değeri tutuldu.
    return en_sonki_liste

#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
def gs(tüm_oyuncuların_bilgileri_liste,eşleşmeler_dict,semboller_dict,en_sonki_liste):#Galibiyet Sayısı hesaplamasını yapıp genel listeye ekliyor.
    for i in range(len(tüm_oyuncuların_bilgileri_liste)):  # her oyuncu için dönecek
        bu_oyuncunun_eşleşme_listesi = eşleşmeler_dict[i + 1]
        bu_oyuncunun_sembol_listesi = semboller_dict[i + 1]
        toplam_puan = 0
        for j in range(len(semboller_dict[i + 1])):  # eşleşme sayısı kadar dönecek
            if  bu_oyuncunun_eşleşme_listesi[j] !=  "BYE":
                if bu_oyuncunun_sembol_listesi[j]=="+"or bu_oyuncunun_sembol_listesi[j]=="1":
                    toplam_puan+=1
        for index in range(len(en_sonki_liste)):
            if en_sonki_liste[index][5] == i + 1:
                en_sonki_liste[index].append(toplam_puan)  # böylece genel bilgiler listesinde son eşitlik bozma ölçütü gs tutuldu.
    return en_sonki_liste
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
def main():
    rakibi_gelmeyip_tur_atlayanlar_listesi=[]
    #Burada ilk girdi çıktılar yapılıyor.
    tüm_oyuncuların_bilgileri_liste,toplam_oyuncu_sayısı=ilk_girdiler()
    tüm_oyuncuların_bilgileri_liste,toplam_oyuncu_sayısı=sıralayıcı(tüm_oyuncuların_bilgileri_liste,toplam_oyuncu_sayısı)
    eşleşmeler_dict,renkler_dict,mac_sonucları_dict,puanlar_dict,semboller_dict=başlangıç_sıralama_yazdır(tüm_oyuncuların_bilgileri_liste,toplam_oyuncu_sayısı)
    #Tur sayısı kontrolü sağlanıyor.
    import math
    ALT_SINIR = int(math.log2(toplam_oyuncu_sayısı)) + 1
    if math.log2(toplam_oyuncu_sayısı) % 1 ==0:
        ALT_SINIR-=1
    UST_SINIR = toplam_oyuncu_sayısı -1
    while True:
        try:
            tur_sayısı = int(input(f"Turnuvadaki tur sayısını giriniz : ({ALT_SINIR}-{UST_SINIR})"))
            while not ALT_SINIR <= tur_sayısı <= UST_SINIR:
                tur_sayısı = int(input(f"Lütfen turnuvadaki tur sayısını yandaki kriterler arasında giriniz : ({ALT_SINIR}-{UST_SINIR})"))
            break
        except:
            True
    ilk_oyuncu_ilk_renk = input("Baslangic siralamasina gore ilk oyuncunun ilk turdaki rengini giriniz (b/s)").upper()
    while ilk_oyuncu_ilk_renk not in [ "B", "S"] or type(ilk_oyuncu_ilk_renk) == int: #Renk kontrolü
        ilk_oyuncu_ilk_renk = input("Lütfen tekrar başlangic siralamasina gore ilk oyuncunun ilk turdaki rengini giriniz (b/s)").upper()
    # Burada eşleştirmedeki ilk renk ataması için ayarlama yapıyorum.
    if ilk_oyuncu_ilk_renk == "B":
        ikinci_oyuncu_ilk_renk = "S"
    else:
        ikinci_oyuncu_ilk_renk = "B"
    for i in range(tur_sayısı):
        tur=i
        eşleşme_sırası_list,eşleşmeler_dict=eşleştir_ve_yazdır(eşleşmeler_dict,renkler_dict,toplam_oyuncu_sayısı,tüm_oyuncuların_bilgileri_liste,kontrol_listesi,ilk_oyuncu_ilk_renk,ikinci_oyuncu_ilk_renk,tur,rakibi_gelmeyip_tur_atlayanlar_listesi,mac_sonucları_dict,semboller_dict)
        tüm_oyuncuların_bilgileri_liste,rakibi_gelmeyip_tur_atlayanlar_listesi=parti_sonuc_alıcı(toplam_oyuncu_sayısı,i+1,tüm_oyuncuların_bilgileri_liste,eşleşme_sırası_list,puanlar_dict,renkler_dict,eşleşmeler_dict,rakibi_gelmeyip_tur_atlayanlar_listesi,semboller_dict,mac_sonucları_dict)
        sıralayıcı(tüm_oyuncuların_bilgileri_liste,toplam_oyuncu_sayısı)
   #-----------------------------------------------------------------------------------------------------------------------------------------------------
    en_sonki_liste=tüm_oyuncuların_bilgileri_liste.copy()
    en_sonki_liste=bh1_bh2(mac_sonucları_dict,semboller_dict,tüm_oyuncuların_bilgileri_liste,tur_sayısı,eşleşmeler_dict,en_sonki_liste)#BH VE BH2 EKLENDİ
    en_sonki_liste=sonneborn(tüm_oyuncuların_bilgileri_liste,eşleşmeler_dict,mac_sonucları_dict,semboller_dict,en_sonki_liste) #SONNEBORN BERGER EKLENDİ
    en_sonki_liste=gs(tüm_oyuncuların_bilgileri_liste,eşleşmeler_dict,semboller_dict,en_sonki_liste) #SON ÖLÇÜT GALİBİYET SAYISI EKLENDİ.
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    en_sonki_liste.sort(reverse=True,key=lambda oyuncu: oyuncu[9])#GS
    en_sonki_liste.sort(reverse=True,key=lambda oyuncu: oyuncu[8])#SN
    en_sonki_liste.sort(reverse=True,key=lambda oyuncu: oyuncu[7])#BH2
    en_sonki_liste.sort(reverse=True,key=lambda oyuncu: oyuncu[6])#BH1
    en_sonki_liste.sort(reverse=True,key=lambda oyuncu: oyuncu[4])#Puan
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    print("NİHAİ SIRALAMA LİSTESİ")
    print("SNo    BSNo    LNo        Ad-Soyad     Elo    Ukd    Puan      BH-1      BH-2      SB      GS")
    print("---    ----    ----     -------------  ----   ----   ----     -----     -----     -----   ----")
    for i in range(toplam_oyuncu_sayısı):
        print(format(i+1,"3d"),end="    ")#SNo
        print(format(en_sonki_liste[i][5],"4d"),end="    ")#BSNo
        print(format(en_sonki_liste[i][0], "4d"), end="    ")#LNo
        print(format(en_sonki_liste[i][1], "13"), end="  ")#AdSoyad
        print(format(en_sonki_liste[i][3], "4d"), end="   ")#Elo
        print(format(en_sonki_liste[i][2], "4d"), end="   ")#UKD
        print(format(en_sonki_liste[i][4], "4g"), end="     ")#Puan
        print(format(en_sonki_liste[i][6], "5g"), end="     ")#BH1
        print(format(en_sonki_liste[i][7], "5g"), end="     ")#BH2
        print(format(en_sonki_liste[i][8], "5g"), end="   ")#SB
        print(format(en_sonki_liste[i][9], "4g"))
        en_sonki_liste[i].append(i+1)
        #Yukarıda en sonki çıktı için Snoları listeye ekledik,10. indexte sıra no lar var
    #------------------------------------------------------------------------------------------------------------------------------------------------------
    en_sonki_liste.sort(key=lambda eleman: eleman[5])#BSNolara göre sıraladık
    #Çapraz Tablo
    print("Çapraz Tablo:")
    print("BSNo    SNo    LNo      Ad-Soyad      Elo     Ukd",end="    ")
    for i in range(tur_sayısı):
        print(i+1,".Tur",end="  ")
    print("Puan    BH1     BH2     SB    GS")
    print("---    ---    ---    -------------    ----    ----",end="   ")
    for i in range(tur_sayısı):
        print("------",end="  ")
    print("----  ------  ------  ------  ---")
    for bu_eleman in en_sonki_liste:#Bsnoya göre sıralaanmış son listedeki her elemanı döndürecek
            print(str(bu_eleman[5]).rjust(3),"  ",str(bu_eleman[10]).rjust(3),"  ",str(bu_eleman[0]).rjust(3),"  ",bu_eleman[1].ljust(13),"  ",str(bu_eleman[3]).rjust(4),"  ",str(bu_eleman[2]).rjust(4),end="    ")
            for i in range(tur_sayısı):
                if eşleşmeler_dict[bu_eleman[5]][i]=="BYE":
                    print("- - 1",end="   ")
                else:
                    print(str(eşleşmeler_dict[bu_eleman[5]][i]).rjust(1),str(renkler_dict[bu_eleman[5]][i]).rjust(1),str(semboller_dict[bu_eleman[5]][i]).rjust(1), end="   ")
            print(str(format(bu_eleman[4],",.2f")).rjust(4),"",str(format(bu_eleman[6],",.2f")).rjust(5)," ",str(format(bu_eleman[7],",.2f")).rjust(5)," ",str(format(bu_eleman[8],",.2f")).rjust(5)," ",str(format(bu_eleman[9],",.2f")).rjust(3))
    #PROGRAM BURADA BİTER
main()
