while True:
    try:
        a=int(input("Enter integer number:"))
        print("integer")
        b=int(input("Enter integer:"))
        c=a/b
        print("Division",c)
        break
    except ValueError:
        print("not integer")
    
    except ZeroDivisionError:
        print("Provide non-zero denominator")
        
    finally:
        print("I will always execute")
        