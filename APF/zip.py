s1= {1,2,3}
s2= {'b', 'a', 'c'}
s3= list(zip(s1,s2))
print(s3,'\n')

l1=[10,20,30,40]
l2=[100,200,300,400]

for x, y in zip(l1,l2[::-1]):
    print(x,y)
    
st=['reliance', 'infoys', 'tcs']
pr=[2175,1127,2750]

nd={st: pr for st, pr in zip(st, pr)}

print('\n{}'.format(nd))