
    
    
#: WAP to find the Body Mass Index of a person using the following formula and conditions.
#BMI=Weight/Height*Height
#BMI <18.0 then Underweight
#BMI >=18.0 and BMI<24.9 then Normal
#BMI >=25 and BMI<30 then Over Weight
#BMI>=30 then Obese

Weight=(input("Enter the Weight of a person"))
Height=(input("Enter the height of a person"))
BMI=Weight//Height*Height
if(BMI<18):
    print("It is underweight")
elif(BMI >=18.0 and BMI<24.9):
    print("it is normal")
elif(BMI >=25 and BMI<30):
    print("It is Overweight")
else:
    print("Obese")

