import turtle

def mid_top():
    t.home()
    t.penup()
    t.left(90)
    t.forward(200)
    t.pendown()

def left_sheild():
    mid_top()
    t.left(215)
    t.circle(150, 90)


def sheild():
    left_sheild()
    #right_sheild()



screan = turtle.Screen()
t = turtle.Turtle()

sheild()
turtle.done()
