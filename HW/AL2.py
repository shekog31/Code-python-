c=input("Enter a character:")

if len(c) !=1:
    print("\nInvalid Input")
else:
    if c.isalpha():
        print(f"\n{c} is an alphabet")
    else:
        print(f"\n{c} is not an alphabet")

        