s=input("Enter word: ")
ch=input("Enter character to find: ")

i=0
co=0


while (i<len(s)):
    if(s[i]==ch):
        co=co+1
    i=i+1

print("The total number of times its said: ", co)