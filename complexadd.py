class Complex:
    def __init__(self,real=0,imaginary=0):
        self.real=real
        self.imaginary=imaginary
        
    def __str__(self):
        return "({0}+{1}i)".format(self.real,self.imaginary)
    
    def __add__(self,obj):
        real=self.real+obj.real
        imaginary=self.imaginary+obj.imaginary
        return Complex(real,imaginary)
    
c1=Complex(1,2)
c2=Complex(5,6)
c3=Complex()
c3=c1+c2
print(c3)