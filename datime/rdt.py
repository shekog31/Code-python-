import random
import time

def grd(sd,ed):
    print("Printing random date between",sd,"and",ed)
    rg=random.random()
    df='%m/%d/%Y'
    
    st=time.mktime(time.strptime(sd,df))
    et=time.mktime(time.strptime(ed,df))
    
    rt=st+rg+(et-st)
    rd=time.strftime(df,time.localtime(rt))
    return rd

print("Random date=",grd("1/1/2025","3/31/2025"))