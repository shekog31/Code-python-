import random

op=['rock','paper','scissors']

uch=input("choose rock, paper or scissors: ")

cch=random.choice(op)

print("Your choice: ",uch)
print("Computer's choice: ",cch)

if uch== cch:
    print("It's a tie")
elif uch =='rock' and cch=='scissors':
    print("You win")
elif uch =='paper' and cch=='rock':
    print("You win")
elif uch =='scissors' and cch=='paper':
    print("You win")
elif uch =='rock' and cch=='paper':
    print("You lose")
elif uch =='paper' and cch=='scissors':
    print("You lose")
elif uch =='scissors' and cch=='rock':
    print("You lose")