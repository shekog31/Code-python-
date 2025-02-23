def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

print("please pick operation")
print("a.add")
print("b.sub")
print("c.mul")
print("d.div")
print("e.mod")
choice=input("Please pick the choice(a/b/c/d/e)")

num1=int(input("enter value 1:"))
num2=int(input("enter value 2:"))

if choice=='a':
    print(num1,"+" ,num2,"=" ,add(num1,num2))
elif choice=='b':
    print(num1,"-" ,num2,"=" ,sub(num1,num2))
elif choice=='c':
    print(num1,"x" ,num2,"=" ,mul(num1,num2))
elif choice=='d':
    print(num1,"/" ,num2,"=" ,div(num1,num2))
elif choice=='e':
    print(num1,"%" ,num2,"=" ,mod(num1,num2))
else:
    print("Input invalid")