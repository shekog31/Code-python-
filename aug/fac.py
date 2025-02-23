def fac(f):
    ''' This is a rec func'''
    
    if f==0 or f==1:
        return 1
    else:
        return f*fac(f-1)
    
print(fac.__doc__)
print("The fac of 0:",fac(0))
print("The fac of 1:",fac(1))
print("The fac of 2:",fac(2))
print("The fac of 3:",fac(3))