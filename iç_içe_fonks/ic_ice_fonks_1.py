

def fonksiyon(*args):#argsın başına * koymak istediğim kadar argüman yazmamı sağlıyor
    for i in args:
        print(i)


fonksiyon(1,2,3)

def fonksiyon2(**kwargs):
    print(kwargs)
    for i,j in kwargs.items():
        print(i,j)

fonksiyon2(isim="aleyna",soyisim="şener",numara=12344)
