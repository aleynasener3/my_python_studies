class Computer():
    def __init__(self,brand,color,ram,price):
        
        self.brand = brand
        self.color = color
        self.ram = ram
        self.price = price

    def __str__(self):
        return " Brand:{} \n Color:{} \n Ram:{} \n Price:{}".format(self.brand,self.color,self.ram,self.price)

    def __len__(self):
        return self.ram
computer = Computer("hp","black",64,1000)

print(computer)
print(len(computer))
