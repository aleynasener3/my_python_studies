import sqlite3

con = sqlite3.connect("kutuphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(İsim TEXT, Yazar TEXT, Yayınevi TEXT,Sayfa_Sayisi INT)")
    con.commit()

def veri_ekle():
    cursor.execute("Insert into kitaplık Values('istanbul','ahmet';'a',921)")
    con.commit()
def veri_ekle2(isim,yazar,yayinevi, sayfa_sayisi):
    
    cursor.execute("insert into kitaplık values (?,?,?,?)",(isim,yazar,yayinevi, sayfa_sayisi))
    con.commit()

def verileri_al():
    cursor.execute("Select * From kitaplık")
    liste=cursor.fetchall()
    for i in liste:
        print(i)

def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık")
    liste = cursor.fetchall
    for i inn liste:
        print(i)
def verileri_al3(yayinevi):
    curser.execute("Select *From kitaplık where Yayınevi=?"i(yayinevi,))
    liste=cursor.fetchall()
    for i in liste:
        print(i)

def verileri_guncelle(eski_yayinevi,yeni_yayinevi):
    cursor.execute("Update kitaplık set Yayınevi =? where Yayınevi=?",(yeni_yayinevi,eski_yayinevi))
    con.commit()

def verileri_sil(yazar):
    cursor.execute("Delete From kitaplık where Yazar=?",(yazar,))
    con.commit()
    
veri_ekle()
    

isim=input("isim:")
yazar=input("yazar:")

yayinevi=input("yayinevi:")

sayfa_sayisi=input("sayfa sayısı:")

veri_ekle2(isim,yazar,yayinevi, sayfa_sayisi)

con.close()
