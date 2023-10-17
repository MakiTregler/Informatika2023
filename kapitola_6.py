import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("darkblue")

wn.exitonclick()

alex.goto(0,0)
drawSquare(alex,20)
alex.penup()
alex.goto(-10,-10)
alex.pendown()
drawSquare(alex,40)
alex.penup()
alex.goto(-20,-20)
alex.pendown()
drawSquare(alex, 60)
alex.penup()
alex.goto(-30,-30)
alex.pendown()
drawSquare(alex, 80)
alex.penup()
alex.goto(-40,-40)
alex.pendown()
drawSquare(alex,100)