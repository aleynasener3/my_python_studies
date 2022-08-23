import os

from datetime import datetime

print(dir(os))#fonksiyon listesi

print(os.getcwd()) #dizinini söylüyor

os.chdir("C:/xxx") #dizin değiştirebiliyoruz

print(os.listdir())#dizindeki dosyaları listeliyor

os.mkdir("deneme1")
os.mkdirs("deneme1/deneme2") #iç içe klasör oluşturuyor

os.rmdir("deneme2/deneme3") #deneme3 silindi

os.removedirs("deneme2/deneme3")#ikisini de siliyor

os.rename("eski.txt","yeni.txt")#ad değiştiriyor

print(os.stat("test.txt")) #özelliklerini söylüyor

print(datetime.fromtimestamp(os.stat("test.txt").st_mtime))#değiştirildiği zamanı söylüyor

for i in os.walk("C:/XXX"):#dosyaları listeliyor
    
    print(i)
