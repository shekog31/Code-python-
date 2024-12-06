n=int(input("Enter a number:"))
s=0

t=n
while t>0:
    d=t%10
    s+=d**3
    t//=10
    
if n==s:
    print(f'{n} is an Armstrong Number')
else:
    print(f"{n} is not an Armstrong Number")