wea=(1,1,1,1,0,0,0)
sunny=0
rainy=0
for i in range(0,7):
    if(wea[i]==0):
        rainy+=1
    else:
        sunny+=1
        
if(sunny>rainy):
    print("Good weather")
else:
    print("Bad weather")