try:
    num=int(input("enter a number:"))
    print("The number is:" ,num)
    
except ValueError as ex:
    print("exception:" ,ex)