class Room:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def getArea(self):
        return (self.length*self.breadth)
    
class Bedroom(Room):
    def __init__(self,length,breadth,height):
        #calls base condtructor i.e. __init__() method
        super().__init__(length,breadth)
        self.height=height
    def getVolume(self):
        return (self.length*self.breadth*self.height)
    
l=int(input("Enter a length:"))
b=int(input("Enter a breadth:"))
h=int(input("Enter a height:"))
Room=Bedroom(l,b,h)
print("The area of bedroom=",Room.getArea())
print("The Volume of bedroom=",Room.getVolume())


