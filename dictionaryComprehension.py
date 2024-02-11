centigrade = {'Kathmandu': 30, "Butwal": 40, "Dharan": 35, "Mustang": 15, "Dhangadi": 42} 
fahrenheit = {key: (value*(9/5)+32) for (key, value) in centigrade.items()} 
print(fahrenheit) 
fahrenheit = {key: round(value*(9/5)+32) for (key, value) in centigrade.items()} 
print(fahrenheit)

weather = {key:"warm" if value >35 else "cold" for (key, value) in centigrade.items()}
print(weather)

#################################
def temp_func(value): 
    if value>40: 
        return "Hot" 
    elif 40<=value>=35: 
        return "Warm" 
    else: 
        return "Cold" 
weather_update = {key:temp_func(value) for (key, value) in centigrade.items()}
print(weather_update)
