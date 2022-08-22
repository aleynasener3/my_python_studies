text = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

def kelime_frekansi(text):
        kelime_sozluk = dict()
        for i in text:
            if (i in kelime_sozluk):
                kelime_sozluk[i]+=1
            else:
                kelime_sozluk[i]=1
        for kelime,sayi in kelime_sozluk.items():
            print("{} kelimesi {} defa geçiyor".format(kelime,sayi))
kelime_frekansi(text)
