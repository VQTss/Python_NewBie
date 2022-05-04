class Student():
    def __init__(self,name,id,contry) :
        self.name   =  name
        self.id     =  id
        self.contry = contry

student1 = Student("Vo Quoc Thai","CE160568","Dong Thap")
print("Name",student1.name)
print("ID",student1.id)
print("Country",student1.contry)
