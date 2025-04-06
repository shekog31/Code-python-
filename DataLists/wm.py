def mw(ws):
    c=0
    l=[]
    for word in ws:
        if len(word)>1 and word[0]==word[-1]:
            c+=1
            l.append(word)
            print("List of words with first and last letter the same :",l)
            return c

count=mw(['abc','mom','zxy','dad','111','123'])
print("number of words that have same first and last letter:",count)