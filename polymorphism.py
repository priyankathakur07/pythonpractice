# compile time polymorphism
'''class maths:
    def addition(self,a=1,b=2,*args):
        result = a+b
        for num in args:
            result += num
        return result
m = maths()
print(m.addition(9,0))
print (m.addition(25,52,52)) '''


# runtime
class A:
    def show(self):
        print("hello from A")
class B(A):
    def show(self):
        print("hello from B")

obj = [A(),B()]                                                                                                                 
for i in obj:
    i.show()