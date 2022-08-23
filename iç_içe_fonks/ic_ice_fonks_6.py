def ekstra(fonk):
    
    def ekstra_ozellik(sayilar):
        print("Mükemmel Sayılar...")
        muk_list=list()
        for sayi in sayilar:
            toplam = 0
            i = 1
            while (i < sayi):
                if (sayi % i == 0):
                    toplam += i
                i +=1
            if (toplam == sayi):
                print(sayi)
                muk_list.append(sayi)
                print(muk_list)

        fonk(sayilar)
        print(muk_list)
                
    return ekstra_ozellik

@ekstra
def asal_sayi(sayilar):
    liste = list()
    for i in sayilar:
        if (i==1):
            pass
        elif (i==2):
            liste.append(2)
        elif (i>2):
            j=2
            x=0
        
            while (j<i):
                
                if(i%j==0):
                    x+=1
                    

                j+=1
            
            if(x==0):
                liste.append(i)

    print("asal",liste)
    

asal_sayi(range(1,100))
