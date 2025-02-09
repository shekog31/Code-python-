import turtle
turtle.Screen().bgcolor("Blue")
sc = turtle.Screen()
sc.setup(400,400)
polygon=turtle.Turtle()

ns=6
sl=70

a=360.0/ns
for i in range(ns):
    polygon.forward(sl)
    polygon.right(a)
    
turtle.done()