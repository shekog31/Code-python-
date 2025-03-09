v=False

while not v:
    try:
        n=int(input("enter a number: "))
        while n%2==0:
            print("even number")
            
        v=True
    except ValueError:
        print("Invalid")