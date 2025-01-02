temp= int(input("Enter temperature outside: "))
j1= int(input("Enter weight of jacket 1 (max 5):"))
j2= int(input("Enter weight of jacket 2 (max 5):"))
j3= int(input("Enter weight of jacket 3 (max 5):"))
jtot= j1+j2+j3

if jtot>=15 and temp>=100:
    print("You will be too hot")
elif jtot>=14 and temp>=90:
    print("You will be hot")
elif jtot>=13 and temp>=80:
    print("You will be warm")
elif jtot>=12 and temp>=70:
    print("You will be warm")
elif jtot>=11 and temp>=60:
    print("You will be fine")
elif jtot>=10 and temp>=50:
    print("You will be cold")
elif jtot>=9 and temp>=40:
    print("You will be very cold")
elif jtot>=8 and temp<=40:
    print("You will be very cold")
elif jtot>=7 and temp<=40:
    print("You will be very cold")
elif jtot>=6 and temp<=40:
    print("You will be very cold")
elif jtot>=5 and temp<=40:
    print("You will be very cold")
elif jtot>=4 and temp<=40:
    print("You will be very cold")
elif jtot>=3 and temp<=40:
    print("You will be very cold")
elif jtot>=2 and temp<=40:
    print("You will be very cold")
elif jtot>=1 and temp<=40:
    print("You will be very cold")
else:
    print("You will be fine")





