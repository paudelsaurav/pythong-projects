class Employee: 
    def __init__(self, firstname, lastname): 
        self.firstname = firstname 
        self.lastname = lastname 
 
    @property 
    def email(self): 
        return '{}.{}@gmail.com'.format(self.firstname, self.lastname) 
 
    @property 
    def fullname(self): 
        return '{} {}'.format(self.firstname, self.lastname) 
 
    @fullname.setter 
    def fullname(self, name): 
        firstname, lastname = name.split(' ') 
        self.firstname = firstname 
        self.lastname = lastname 
 
    @fullname.deleter 
    def fullname(self): 
        print("deleter property") 
        self.firstname = None 
        self.lastname = None 
 
emp = Employee("Saurav", "Paudel") 
emp.fullname = "Abhishek Chapagain"  # what if we assign fullname? 
print(emp.firstname) 
print(emp.email)  # using function as attribute 
print(emp.fullname)  # using function as attribute 
 
del emp.fullname 
print(emp.fullname)

