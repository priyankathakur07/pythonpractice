class A:
    def hello():
        print("hello")
class B:
    def hello():
        print("hey")
class C(A,B):
    def __init__(self):
        print("constructor")
obj = C()
print(C.mro())
print(C.__mro__)
