print("Full diamond")
rows=int(input("Enter number of rows:"))

for i in range(1,rows+1):
    print("  " * (rows-i),end=" ")
    print(" * " * i)

for i in range(rows,0,-1):
    print("  " * (rows-i),end=" ")
    print(" * " * i)