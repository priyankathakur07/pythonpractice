'''class person:
    def __init__(self,name,age):
        self.name = name # public
        self.__age = age # private property
p1 = person("harry",8)
print(p1.name)
print(p1.__age) # it is giving error because accessing private
'''
class hello:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age
h1 = hello('xyz',0)
print(h1.get_age())
