class Time():
    def __init__(self,year,month,day,hour):
        self.year=year
        self.month=month
        self.day=day
        self.hour=hour

    
    @classmethod
    def converter(this,inputhour):
        d=input//24
        rh=input%24
        m=d//30
        rd=d%30
        y=m//12
        rm=m%12
        return this(y,rm,rd,rh)
    def show(self):
        return f'{self.year}:{self.month},{self.day}:{self.hour}'
    
hours=int(input("enter the hours:"))
if hours>=10000:
    date=hours.Converter(hours)
    print(date.show())