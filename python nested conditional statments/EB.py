u=float(input("Enter energy used:"))

bill=0.0

if u<=100:
    bill=u *3.0
else:
    if u<=200:
        bill=(100*3.0)+((u-100)*5.0)
    else:
        bill=(100*3.0)+(100*5.0)+(100*7.0)+((u-300)*10)
print("Your EB is:",bill)
