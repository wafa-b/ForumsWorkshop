class Member:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.id = 0


    def __str__(self):
        return  "Name: " + self.name + "\n" +"Age: " + str(self.age)

class Post:
    def __init__(self,title,contente):
        self.title = title
        self.contente = contente
        self.id = 0


    def __str__(self):
        return "Title: " +self.title + "\n"+ "Contente: "+ self.contente
