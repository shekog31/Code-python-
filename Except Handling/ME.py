try:
    num1,num2=eval(input("enter 2 numbers, seperated by a comma:"))
    re=num1/num2
    print("Result is:",re)
    
except ZeroDivisionError:
    print("Division by 0 is not possible")
    
except SyntaxError:
    print("COmma is missing, enter value using a comma like 1,2")
    
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will be executing no matter what")
    