from datetime import datetime

su_an = dateteime.now
print(su_an.year)
print(su_an.month)

print(su_an.hour)

print(datetime.ctime(su_an))

print(datetime.strftime(su_an,"%D"))

# %X şeklinde gösterilir y yıl b ay a gün x saat d gün

locale.setlocale(locale.LC_ALL,"")

print(datetime.strftime(su_an,"%Y %B"))

saniye = datetime.timestamp(su_an)

print(saniye)

su_an2= datetime.fromtimestamp(saniye)

tarih=datetime(2019,12,1)#yıl ay gün



