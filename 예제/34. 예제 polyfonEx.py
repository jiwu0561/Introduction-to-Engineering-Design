import turtle as t

no=4
t.color("blue")

def drawPoly():
    for i in range(no):
        t.fd(50)
        t.lt(360/no)

def draw(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    drawPoly()
    t.end_fill()

def set_3():
    global no
    no = 3

def set_4():
    global no
    no = 4

def set_5():
    global no
    no = 5

t.onscreenclick(draw)

t.onkey(set_3, "3")
t.onkey(set_4, "4")
t.onkey(set_5, "5")

t.listen()
t.mainloop()