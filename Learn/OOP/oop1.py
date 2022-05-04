class Item():
    def __init__(self,name,price,quatity):
        self.name    = name # Attribute instance
        self.price   = price
        self.quatity =  quatity

item1 = Item("Phone",1000,3) # Object
print("Name of item1    =",item1.name)
print("Price of item1   =",item1.price)
print("Quatity of item1 =",item1.quatity)
