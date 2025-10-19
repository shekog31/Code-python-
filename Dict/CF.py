t_d={'Coding':2, 'is':2, 'great':1}

print("The original dictionary:" + str(t_d))

K=2

res=0
for key in t_d:
    if t_d[key]==K:
        res=res+1
        
print("frequency of K is:" + str(res))