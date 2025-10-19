n1=[2,4,6]
n2=[8,10,12]
re=map(lambda x, y: x+y, n1, n2)
print("Addition of lists")
print(list(re))

ns=[1,2,3,4,5]
def sq(n):
    return n*n
square= list(map(sq, ns))
print("Square of numbers in list")
print(square)