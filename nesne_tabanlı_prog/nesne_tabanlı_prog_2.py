class Yazilimci():

    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller

    def show_info(self):
        print("""
        özellikler
        isim: {}
        soy isim: {}
        numara: {}
        maaş: {}
        diller: {}

        """.format(self.isim,self.soyisim,self.numara,self.maas, self.diller))

    def add_salary(self,zam_miktari):
        print("zam yapılıyor")
        self.maas+=zam_miktari

    def add_language(self,yeni_dil):
        print("dil ekleniyor")
        self.diller.append(yeni_dil)

yazilimci = Yazilimci("aleyna","şener","12565",30000,["python","java","c"])

yazilimci.show_info()
