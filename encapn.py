'''class employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary # private attributes


emp = employee("fedrick",5000)
print (emp) # nothing will printed in this only object at is printed
print(emp.name)
print(emp.__salary)
'''


# how to print this print(emp)
class employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary # private attributes

    # A method to control what print() displays
    def __str__(self):
        return f"employee:{self.name},salary :{self.__salary}"

emp = employee("fedrick",5000)
print (emp) 
