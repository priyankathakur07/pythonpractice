from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def show(self):
        pass
class eng(Greet):
    def run(self):
        return("hello")
g = eng()
print (g.run())
#print(g.show()) 