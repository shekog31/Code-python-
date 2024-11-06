print("Select your ride (1 is bike or 2 is car): ")
r=int(input("Select your ride: "))
if(r==1):
    print("What type of bike (1 or 2): ")
    print("1. Scooter 2. Motorbike")
    sm=int(input("Select your bike type: "))
    if(sm==1):
        print("You have selected Scooter")
    else:
        print("You have selected Motorbike")
elif(r==2):
     print("What type of car (1 or 2): ")
     print("1. Racecar 2. Van")
     rv=int(input("Select your car type: "))
     if(rv==1):
        print("You have selected Racecar")
     else:
        print("You have selected Van")
else:
    print("You don't get a vehicle.")
    
    