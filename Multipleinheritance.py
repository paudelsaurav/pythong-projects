class Calculation1:
    def Summation(self,a,b):
        return a+b
    
class Calculation2:
    def Multiplication(self,a,b):
        return a*b
    
class Overall(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b
    
ol=Overall()
print("The summation is",ol,Summation(3,4,5))
print("The Multiplication is",ol,Multiplication(3,4)) 
print("The division is",ol,Divide(3,2)) 
    
