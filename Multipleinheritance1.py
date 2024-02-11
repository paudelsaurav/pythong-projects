class Car:
    def __init__(self):
        print("Car Constructor")
    def VehicleType(self):
        print("It is a car")
        
class Maruti(Car):
    def __init__(self):
        print("Maruti Constructor")
    def speed(self):
        print("Speed of 80 km/hr")
        
class Maruti800(Maruti):
    def __init__(self):
        print("Maruti800 constructor")
    def speed(self):
        print("Speed of 120km/hr")
        
car=Maruti800()
car.VehicleType()
car.speed()






class Grandfather:  # base class 
    def __init__(self):  # constructor 
        print('Grandpa - Hii') 
 
    def age(self, a):  # method 
        print('Printing the age of grandpa : ', a) 
 
class Father(Grandfather):  # derived class level 1 
    def __init__(self):  # constructor 
        print('Father - Hii') 
        super().__init__()  # calling base constructor 
 
    def age(self, a):  # method overriding 
        print('Printing the age(Father): ', a) 
        super().age(a + 20)  # calling base class's method age() 
 
class Mother(Father):  # derived class level 2 
    def __init__(self):  # constructor 
        print('Mother - Hii') 
        super().__init__()  # calling base constructor 
 
    def age(self, a):  # method overriding 
        print('Printing the age(Mother): ', a) 
        super().age(a + 5) 
 
# Main function 
if __name__ == '__main__': #executing the code from the current file 
    o = Mother() 
    o.age(30) 