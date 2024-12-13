h=int(input("Enter a 4 digit number: "))
t=h
hlen=0

while t>0:
    hlen=hlen+1
    t=int(t/10)
    
if h>=4:
    hlen=int(hlen/2)
    ck=0
    mi=0
    mi2=0
    while h>0:
        rm=h%10
        if ck==hlen:
            mi=rm
        elif ck==(hlen-1):
            mi2=rm
        h=int(h/10)
        ck=ck+1
    pr=mi*mi2
        
    print("Product of the mid values: ",pr)
        
else:
    print("Its not a 4 or more digits")