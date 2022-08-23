import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


class Dosya():
    def __init__(self):
        with open("mailler.txt","r",encoding="utf-8") as file:
            dosya_icerigi = file.read()
            link = dosya_icerigi.split("\n")
            self.mail= list()

            for i in link:
                if(i.endswith(".com") and i.find("@")):
                    self.mail.append(i)
            send_list=self.mail
            print(self.mail)

dosya= Dosya()

mesaj = MIMEMultipart()

for i in dosya.mail:
    mesaj["From"]="aleyna@gmail.com"
    mesaj["To"]=i
    mesaj["Subject"]="Smtp mail gönderme"

    yazi="deneme maili"

    mesaj_govdesi = MIMEText(yazi,"plain")
    mesaj.attach(mesaj_govdesi)

    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)

        mail.ehlo()

        mail.starttls()

        mail.login("","")

        mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

        print("Mail Başarıyla Gönderildi....")

        mail.close()

    except:
        sys.stderr.write("Bir sorun oluştu!")
        sys.stderr.flush()


        
