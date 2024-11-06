name=input("What is your name?:")

em=input("Do you have an emergency? (Yes or No):")

att=int(input("Enter your attendance percentage:"))

if em=='Yes':
    if att==75:
        print("Allowed")
    else:
        print("Not allowed")
else:
    print("Not allowed")