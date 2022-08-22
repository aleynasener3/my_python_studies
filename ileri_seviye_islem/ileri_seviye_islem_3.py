class Dosya():
    def __init__(self):
        with open("siir.txt","r",encoding = "utf-8") as file:
            siir_icerigi = file.read()

            satirlar = siir_icerigi.split("\n")
            print(satirlar)

dosya=Dosya()


