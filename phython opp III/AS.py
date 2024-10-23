a=int(input("Enter speed 1:"))
b=int(input("Enter speed 2:"))
c=int(input("Enter speed 3:"))

d=(a+b+c)/3

print("The average speed is:" ,d)

if d>a and d>b and d>c:
    print(" %d is higher than %d,%d,%d" %((d,a,b,c)))
elif d>a and d>b:
   print(" %d is higher than %d,%d,%d" %((d,a,b))) 
elif d>a and d>c:
    print(" %d is higher than %d,%d,%d" %((d,a,c))) 
elif d>b and d>c:
    print(" %d is higher than %d,%d,%d" %((d,b,c))) 
elif d>a:
    print(d,a)
elif d>b:
    print(d,b)
elif d>c:
    print(d,c)
else:
    print("Input valid")
    
        