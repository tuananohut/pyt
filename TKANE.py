kayranın_kredi_kart_nosu = 7821212451
kayranın_kredi_kart_şifresi= 6458
kayranın_parası=15000
tuananın_kredi_kart_nosu = 9563214789
tuananın_kredi_kart_şifresi= 8179
tuananın_parası=15000
ervanın_kredi_kart_nosu = 1575154521
ervanın_kredi_kart_şifresi= 5858
ervanın_parası=15000
hesapvar=1
hesapyok=0
yatırmak = 1
cekmek = 2 
hicbir_sey= 3
for i in range(5):
    print("tkane kredi kartı işlemleri merkezine hoşgeldiniz. Yanlış bir şey yaptığınızda 5 kez tekrar edebilirsiniz!")
    hesap = int(input("Merhaba. Bir hesabınız var mı? Varsa 1'i yoksa 0'ı tuşlayınız."))
    if hesap == hesapvar:
        kredi_kart_no = int (input("Kredi kart numaranızı giriniz:"))
        if kredi_kart_no == kayranın_kredi_kart_nosu:
            print("Hoşgeldin Kayra. Senin olduğunu tespit etmem için lütfen kredi kart şifreni gir.")
            sifre_1=int(input("Şifrenizi giriniz:"))
            if sifre_1 == kayranın_kredi_kart_şifresi:
                print("Tekrardan hoşgeldin Kayra.")
                print("Para yatırmak için 1'e tıklayınız:","Para çekmek için 2'ye tıklayınız:","Hiçbir şey yapmak istemiyorsanız 3 ' e tıklayınız:")
                soru_1 = int(input("Ne yapacaksınız? :"))
                if soru_1 == yatırmak:
                    a = int(input("Ne kadar para yatıracaksınız? :"))
                    sonuc_1 = kayranın_parası + a
                    print("Artık bu kadar paran var:",sonuc_1,"Bizi seçtiğiniz için teşekkürler!")
                    break
                if soru_1 == cekmek:
                    b = int (input("Ne kadar para çekeceksiniz? :"))
                    sonuc_2 = kayranın_parası - b
                    print("Artık bu kadar paran var:",sonuc_2,"Bizi seçtiğiniz için teşekkürler.")
                    break
                if soru_1 == hicbir_sey:
                    print("İnşallah bizi seçmediğiniz için pişman olursunuz!")
                    break
                if soru_1 >= 4:
                    print("Tekrar deneyin!")
        if kredi_kart_no == tuananın_kredi_kart_nosu:
            print("Hoşgeldin Tuana. Senin olduğunu tespit etmem için lütfen kredi kart şifreni gir.")
            sifre_2=int(input("Şifrenizi giriniz:"))
            if sifre_2 == tuananın_kredi_kart_şifresi:
                print("Tekrardan hoşgeldin Tuana.")
                print("Para yatırmak için 1'e tıklayınız:","Para çekmek için 2'ye tıklayınız:","Hiçbir şey yapmak istemiyorsanız 3 ' e tıklayınız:")
                soru_2 = int(input("Ne yapacaksınız? :"))
                if soru_2 == yatırmak:
                    c = int(input("Ne kadar para yatıracaksınız? :"))
                    sonuc_3 = tuananın_parası + c
                    print("Artık bu kadar paran var:",sonuc_3,"Bizi seçtiğiniz için teşekkürler!")
                    break
                if soru_2 == cekmek:
                    d = int (input("Ne kadar para çekeceksiniz? :"))
                    sonuc_4 = tuananın_parası - d
                    print("Artık bu kadar paran var:",sonuc_4,"Bizi seçtiğiniz için teşekkürler.")
                    break
                if soru_2 == hicbir_sey:
                    print("İnşallah bizi seçmediğiniz için pişman olursunuz!")
                    break
                if soru_2 >= 4:
                    print("Tekrar deneyin!")
        if kredi_kart_no== ervanın_kredi_kart_nosu:
            print("Hoşgeldin Erva. Senin olduğunu tespit etmem için lütfen kredi kart şifreni gir.")
            sifre_3=int(input("Şifrenizi giriniz:"))
            if sifre_3 == ervanın_kredi_kart_şifresi:
                print("Tekrardan hoşgeldin.")
                print("Para yatırmak için 1'e tıklayınız:","Para çekmek için 2'ye tıklayınız:","Hiçbir şey yapmak istemiyorsanız 3 ' e tıklayınız:")
                soru_3 = int(input("Ne yapacaksınız? :"))
                if soru_3 == yatırmak:
                    e = int(input("Ne kadar para yatıracaksınız? :"))
                    sonuc_5 = ervanın_parası + e
                    print("Artık bu kadar paran var:",sonuc_5,"Bizi seçtiğiniz için teşekkürler!")
                    break
                if soru_3 == cekmek:
                    f = int (input("Ne kadar para çekeceksiniz? :"))
                    sonuc_6 = ervanın_parası - f
                    print("Artık bu kadar paran var:",sonuc_6,"Bizi seçtiğiniz için teşekkürler.")
                    break
                if soru_3 == hicbir_sey:
                    print("İnşallah bizi seçmediğiniz için pişman olursunuz!")
                    break
                if soru_3 >= 4:
                    print("Tekrar deneyin!")
    if hesap == hesapyok:
        print("Üye olmak için 1'e, olmamak için 0'a tıklayınız.")
        üyeolmak=int(input("Üye olmak ister misiniz?"))
        if üyeolmak == 1:
            print("Merhaba. Şimdi sizden adınızı, istediğiniz 10 haneli kredi kart numaranızı ve kredi kart şifrenizi girmenizi isteyeceğim.")
            Ad=str(input("Adınız nedir?"))
            for j in range(3):
                Kartno=int(input("Kart numaranızı giriniz:"))
                if 1000000000<=Kartno<=9999999999:
                    sifre=int(input("Şifrenizi giriniz:"))
                    break
                else:
                    print("10 haneli girmeniz gerekmektedir.")
            print("Üye olduğunuz için teşekkürler",Ad ,"Ne yapmak istersin?")
            print("Para yatırmak için 1'e tıklayınız:","Para çekmek için 2'ye tıklayınız:","Hiçbir şey yapmak istemiyorsanız 3 ' e tıklayınız:")
            soru_4 = int(input("Ne yapacaksınız? :"))
            if soru_4 == yatırmak:
                g = int(input("Ne kadar para yatıracaksınız? :"))
                sonuc_7 = 0 + g
                print("Artık bu kadar paran var:",sonuc_7,"Bizi seçtiğiniz için teşekkürler!")
                break
            if soru_4 == cekmek:
                h = int (input("Ne kadar para çekeceksiniz? :"))
                sonuc_8 = 0 - h
                print("Artık bu kadar paran var:",sonuc_8,"Bizi seçtiğiniz için teşekkürler.")
                break
            if soru_4 == hicbir_sey:
                print("İnşallah bizi seçmediğiniz için pişman olursunuz!")
                break
            if soru_4 >= 4:
                print("Tekrar deneyin!")
        if üyeolmak==0:
            print("Emin misin?")