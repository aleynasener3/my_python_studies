def kareleri_al():#bu sayede hafızada yer kaplamıyor
    for i in range(1,6):
        yield i**2

generator = kareleri_al()

iterator = iter(generator)
print(next(iterator))


generator2= (i*3 for i in range(5))
iterator2=iter(generator2)
print(next(iterator2))

def carpım_tablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{}x{}={}".format(i,j,i*j)


for i in carpım_tablosu():
    print(i)
