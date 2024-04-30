import turtle as t

def drawRect():
    for i in range(4):
        t.fd(50)
        t.lt(360/4)

def draw(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    drawRect()
    t.end_fill()

def redc():
    t.color("red")

def greenc():
    t.color("green")

def bluec():
    t.color("blue")

t.onscreenclick(draw)

t.onkey(redc, "r")
t.onkey(greenc, "g")
t.onkey(bluec,"b")

t.listen()
t.mainloop()