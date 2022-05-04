class Car:
    def __init__(self,brand,model, founded_year,price):
        self.brand = brand
        self.model = model
        self.founded_year = founded_year
        self.price = price
    
    @classmethod
    def Analys_String(cls,car_string):
        brand,model, founded_year,price = car_string.split('-')
        founded_year = int(founded_year)
        price = int(price)
        return cls(brand,model, founded_year,price)
    @staticmethod 
    def checkPrice(price):
        if price >= 1000:
            return 'This car is expensive'
        else:
            return 'This car is cheap'
    @staticmethod
    def count(value):
        value += 1
        return value
car_template = "Toyota-Camry-1969-800"
car_3 = Car.Analys_String(car_template)
print(car_3.brand)
print(car_3.founded_year)
print(car_3.model)
print(car_3.price)
car_1 =  Car('Vinfast','LuxA',2017,1000)
print(car_1.checkPrice(car_1.price))
print(car_3.checkPrice(car_3.price))
print(car_1.count(1))
print(car_3.count(1))
