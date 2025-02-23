def c(num):
    return num**3

def bc(num):
    if num%3==0:
        return c(num)
    else:
        return False
    
a=int(input("Value:"))
print(bc(a))
