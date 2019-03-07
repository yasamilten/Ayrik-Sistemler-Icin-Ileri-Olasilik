# Numara      : 185112012 
# Ad Soyad    : Yaşam İLTEN      
# Ders        : Ayrık Sistemler İçin İleri Olasılık
# Ödev No     : 1


"""
Soruda verilen dizi içerisinde toplamı 10 olacak şekilde kaç tane ikili sayı var bulunur ve bulunan ikili sayısı bize grup sayısını yani
güvercin yuvası sayısını verir.. İkili sayı dışında kalan herhangi bir sayı olur buda gruba eklenir.
"""
def guvercinYuvasiSayisiniBul(dizi): 
    yuvaSayisi=0;
    index=0;
    i=1;

    while i < len(dizi):
        if (dizi[index]+dizi[i])==10 :
            yuvaSayisi+=1;
            dizi.remove(dizi[i]);
            dizi.remove(dizi[index]);
            i=1;
        else:
          i+=1;

    if len(dizi)>0:
        yuvaSayisi+=1;

    return yuvaSayisi;


#Güvercin yuvası prensibine göre sonuç bulan fonksiyon.
def guvercinYuvasiPrensibi(guvercinSayisi,yuvaSayisi):
    if guvercinSayisi<=yuvaSayisi:
        return 1;
    else:
        return int(guvercinSayisi/yuvaSayisi);

def main():
    print("“S={1,2,3,4,5,6,7,8,9} kümesinin 6 elamanlı her hangi bir altkümesinde toplamı 10 olan iki sayı vardır” ifadesini gösteriniz.")
    yuvaSayisi=guvercinYuvasiSayisiniBul([1,2,3,4,5,6,7,8,9])
    guvercinSayisi=6; # 6 elemanlı herhangi bir altküme guvercin yuvası prensibine göre güvercin sayısına karşılık gelmektedir.
    
    sonuc=guvercinYuvasiPrensibi(guvercinSayisi,yuvaSayisi)
    print("\nGüvercin yuvası prensibine göre sonuç :",sonuc);

    print("\nBu durumda 5 gruptan 6 sayı almamız gerekmektedir. Güvercin yuvası ilkesine göre en az bir gruptan iki elaman almamız gerekir. Bu da, her zaman toplamı 10 olan en az bir ikili seçilecek demektir.")

if __name__=='__main__':
    main();
