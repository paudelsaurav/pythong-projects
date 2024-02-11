class attributes:
    def __init__(self):
        self.public="public attribute"
        self._protected="protected attribute"
        self.__private="private attribute"
        
obj=attributes()
print(obj.public)
print(obj._protected)
print(dir(obj)) 
print(obj._attributes__private)#mangling 


































