class parent:
    def __init__(self):
        self.__salary = 4555
class child(parent):
    def show(self):
        print(self._parent__salary) # acessing private
c = child()
c.show()