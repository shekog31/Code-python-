import random

ntg=random.randint(1,10)

g=None
a=0

print("Welcome to number guessing game, think of a number from 1-10")

while g!=ntg:
    try:
        g=int(input("enter a guess: "))
        a+=1
        
        if g<ntg:
            print("Too low")
        elif g>ntg:
            print("Too High")
        else:
            print("You guessed it")
    except ValueError:
        print("Please enter a valid number")