class Kuvvet2():
    def __init__(self,maximum=0):
        self.maximum=maximum
        self.kuvvet=0
        self.i=1

    def __iter__(self):
        return self

    def __next__(self):
        if (self.kuvvet<=self.maximum):
            sonuc = self.i**2
            self.kuvvet+=1
            self.i+=1
            return sonuc
        else:
            self.kuvvet=0
            raise StopIteration

kuvvet = Kuvvet2(4)

for i in kuvvet:
    print(i)
