import time

def zaman_hesapla(func):
    def wrapper(sayilar):
        baslama=time.time()

        sonuc =func(sayilar)

        bitis=time.time()

        print(func.__name__+" "+str(bitis-baslama)+"saniye sürdü")
    return wrapper
@zaman_hesapla
def kare_hesap(sayilar):

    sonuc = list()
    for i in sayilar:
        sonuc.append(i**2)
    return sonuc
@zaman_hesapla

def kup_hesap(sayilar):
    sonuc=list()
    for i in sayilar:
        sonuc.append(i**3)

    return sonuc

kare_hesap(range(1000))

kup_hesap(range(1000))
    
