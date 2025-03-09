def ea(age):
    
    if age<0:
        raise ValueError("only positive allowed")
    if age%2==0:
        print("age is even")
    else:
        print("age is odd")
        
try:
    n=int(input("Enter your age:"))
    ea(n)
    
except ValueError:
    print("Only positive intergers are allowed")
    
except:
    print("Something is wrong")