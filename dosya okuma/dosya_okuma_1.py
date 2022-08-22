file = open("aa.txt","w",encoding="utf-8")

file.write("word1 \nword2 \nword3")

file.close()

file = open("aa.txt","r",encoding="utf-8")

for i in file:
    print(i)

print("--------------")

file.close()

file = open("aa.txt","r",encoding="utf-8")

info = file.read()

print(info)

file.close()

#file.readline() ilk satırı tanımlar

file = open("aa.txt","r",encoding="utf-8")
liste = file.readlines()
print(liste)
file.close()
