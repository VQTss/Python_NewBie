from telnetlib import DO


class Wolf:
    def __init__(self,name, color):
        self.name = name
        self.color = color
    
    def bark(self):
        print("Grr......")
class Dog(Wolf):
    def bark(self):
        print("Woof")
        print(self.name)

husky = Dog("Max","Red")
husky.bark()    