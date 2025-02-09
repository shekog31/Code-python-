import turtle
turtle.Screen().bgcolor("light blue")
sc = turtle.Screen()
sc.setup(400,400)
st=turtle.Turtle()
si=0
while True:
    for i in range(6):
        st.fd(si+1)
        st.left(26)
        si=si-7
    si=si+1
    