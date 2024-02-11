class square():
    side =8
    def area(self):
        return self.side**2
    
# instantiation -> object creation
sq= square()
print(sq.area())
print(square.area(sq))
sq.side = 10
print(sq.area())

class Price(): 
    def final_price(self, vat, discount=0): 
        """Returns price after applying vat and fixed discount.""" 
        return (self.net_price * (100 + vat) / 100) - discount 
 
p1 = Price() 
p1.net_price = 100 
print(Price.final_price(p1, 20, 10))  
print(p1.final_price(20, 10))  

#    __init__(self) -> inbuilt function called while object creation. can be called initializer or coinstructer
# how to use constructor or initializer

class rectangle():
    def __init__(self,length,breadth):
        self.length= length
        self.breadth= breadth
    def area(self):
        return self.length*self.breadth
len= int(input("enter the length of rectangle"))
bre= int(input("enter the breadth of rectangle"))
r1=rectangle(len,bre)
print("The area of rectangle is",r1.area())
#
class Employee():
    def __init__(self,salary):
        self.salary=salary
#Derived class
class Programmer(Employee):  #IS-A-Relationship-Programmer is an employee 
    def __init__(self,salary,bonus):
        super().__init__(salary)  #salary will be initiated from base class
        self.bonus = bonus
        
class MobileDeveloper(Programmer):   #MobileDeveloper is a Programmer
    def __init__(self,salary,bonus,allowance):
        super().__init__(salary,bonus)
        self.allowance = allowance
        
    def TOralSal(self):
        return self.salary+self.bonus+self.allowance
    
developer = MobileDeveloper(50000,10000,15000)
print("Total Salary of a Mobile develop=",developer.TotalSal())