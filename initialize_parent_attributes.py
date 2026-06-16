class school :
    def __init__(self,id,name):
        self.id = id
        self.name = name
class student(school):
    def __init__(self,id,name,email):
        super().__init__(id,name)   # take from class school
        self.email = email

s = student('harry',9,'harry@gmail.com')
print(s)  # it will print object value
print(s.name,s.email,s.id)
print(s.email)