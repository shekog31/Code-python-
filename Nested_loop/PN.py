l=int(input("Enter the lowest number: "))
u=int(input("Enter highest number: "))

print(f"The prime numbers between {l} and {u} are: ")

for num in range(l,u+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)