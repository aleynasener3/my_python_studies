def anafonks(islem_adi):
    def toplama(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam

    def carpma(*args):
        carpim=1
        for i in args:
            carpim*=i

        return carpim

    if islem_adi=="toplama":
        return toplama
    else:
        return carpma

fonk=anafonks("carpma")
print(fonk(1,2,3))
