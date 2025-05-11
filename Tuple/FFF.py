def palin(r):
    e=len(r)-1
    s=0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True

r=(2,4,6,6,4,2)

if(palin(r)):
    print("Its a flipflop")
else:
    print("Its not a fliflop")