import os

sd=input("Do you want to shutdown?")
if sd=="No" or sd=="no":
     exit()
else:
    os.system("shutdown /s /t 1")