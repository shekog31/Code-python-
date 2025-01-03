rows=int(input("ENter the rows:"))

n=1

print("Floyd's triangle")

for i in range(1,rows+1):
    for j in range(1, i+1):
        print(n,end="")
        n=n+1
    print()