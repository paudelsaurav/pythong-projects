def func(**kwargs):
    print(kwargs)
    
    #All calls equivalent,they print {'a':1,'b':42}
func(a=1,b=42)
func(**{'a':1,'b':42})
func(**dict(a=1,b=42))



#     **kwargs
#This type of keyword arguments is used to hold a dictionary as argument in any function
# eg: def dictfunc(**kwargs):
#               print(kwargs)

    