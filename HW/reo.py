n=1081
rn=0
while n != 0:
    d = n % 10
    rn = rn * 10 + d
    n //= 10

print("Reversed Number: " + str(rn))