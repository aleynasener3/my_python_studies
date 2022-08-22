class Dosya():
    def __init__(self):
        with open("mailler.txt","r",encoding = "utf-8") as file:
            dosya_icerigi=file.read()
            link=dosya_icerigi.split("\n")
            self.mail=list()
            for i in link:
                if (i.endswith(".com") and i.find("@")):
                    self.mail.append(i)

            print(self.mail)

dosya = Dosya()
