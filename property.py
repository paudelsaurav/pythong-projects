class Employee:
    def __init__(self,firstname, lastname):
        self.firstname = firstname 
        self.lastname = lastname 
        self.email = firstname+"."+lastname+"@gmail.com" 
 
    def fullname(self): 
        return '{} {}'.format(self.firstname, self.lastname) 
emp=Employee("Saurav","Paudel") 
emp.firstname="saurav" 
print(emp.firstname)
print(emp.email) 
print(emp.fullname())



#By using function
class Employee: 
    def __init__(self, firstname, lastname): 
        self.firstname = firstname 
        self.lastname = lastname 
 
    def email(self): 
        return '{}.{}@gmail.com'.format(self.firstname, self.lastname) 
 
    def fullname(self): 
        return '{} {}'.format(self.firstname, self.lastname) 
 
emp = Employee("Saurav", "Paudel") 
emp.firstname = "saurav" 
print(emp.firstname) 
print(emp.email()) 
print(emp.fullname()) 

#By using property decorator
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
emp = Employee("Saurav", "Paudel") 
emp.firstname = "saurav" 
print(emp.firstname) 
print(emp.email)#using function as attribute 
print(emp.fullname)#using function as attribute 


