import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("pink")

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

def drawPoly (t, ss, sz)
    """Get turtle t to draw a polygon of sz size"""

    for i in range(4)
        t.forward(sz)
        t.left(135)

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("darkblue")

wn.exitonclick()

tess.goto(0,0)
drawPoly(tess, 8, 50)

tess.goto(0,0)
drawPoly(tess, 8, 50)

# PrettyPattern

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("darkblue")
alex.speed(100)

color = ["darkblue", "orange", "darkgreen", "yellow"]
wn.exitonclick()

alex.goto(0,0)
for n in range(20):
    alex.color(color[n % len(color)])
    alex.left(360/20)
    drawSquare(alex, 80)
