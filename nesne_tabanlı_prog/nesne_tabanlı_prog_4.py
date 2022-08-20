class Book():
    def __init__(self,name,author,page_num,genre):
        self.name = name
        self.author = author
        self.page_num = page_num
        self.genre = genre

    def __str__(self):
        return "Name: {} \n Author: {} \n Page number: {} \n Genre: {}".format(self.name,self.author,self.page_num,self.genre)

    def __len__(self):
        return self.page_num


book = Book("aa","bb",999,"crime")


print(book)
print(len(book))
