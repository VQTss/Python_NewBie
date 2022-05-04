class Empolyee:
    coo_salary = 1.4
    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first + '.' + last  + '@gmail.com'
    def fullName(self):
        return f'{self.first} {self.last}'
    
    def apply_co_salary(self):
       return int(self.pay * self.coo_salary)
    
class Develop(Empolyee):
    co_salary = 1.2
    def __init__(self, first, last, pay,program_language):
        super().__init__(first, last, pay)
        self.program_language = program_language

class  Manage(Empolyee):
    co_salary = 1.5
    def __init__(self, first, last, pay,list_employee = None):
        super().__init__(first, last, pay)
        if list_employee == None:
            self.list_employee = []
        else:
            self.list_employee = list_employee
    
    def add_employee(self, employee):
        if employee not in self.list_employee:
            self.list_employee.append(employee)

    def  remove_employee(self, emp):
        if emp in self.list_employee:
            if emp in self.list_employee:
                self.list_employee.remove(emp)
    def print_emp(self):
        for emp in self.list_employee:
            print('--',emp.fullName())




dev_1 = Develop('Thai','Vo',400,'Python')
print(dev_1.email)
print(dev_1.apply_co_salary())
dev_2 = Develop('Thai','Tran',4000,'Python')
dev_3 = Develop('Phu','Vo',5000,'JS')
man_1 = Manage('Trump','Donal',1000,[dev_1,dev_2])
man_1.remove_employee(dev_1)
man_1.add_employee(dev_3)
man_1.print_emp()