class Point(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return"{0},{1}".format(self.x,self.y)
    def __add__(self,obj):
        x=self.x+obj.x
        y=self.y+obj.y
        return Point(x,y)
    
    
p1=Point(3,4)
p2=Point(5,6)
p3=p1+p2
print(p3)