def asal_sayi():
    for i in range (2,5):
        if(i==2):
            yield i
        
        elif (i>2):
            j=2
            x=0
            while (j<=i):
                
                if (i%j==0):
                    x+=1
                    
                    
                j+=1
            if (x==0):
                
                yield i
            
for sayi in asal_sayi():
    print(sayi)


