l=[1,2,3,4,5,6,7,8,9]

count=0
for i in l:
    count +=1
    
avg=count/len(l)
print("Count",count)
print("Average",avg)

l.sort()
print(l)
print("Smallest value",l[0])
print("Largest value",l[-1])