# p.176 6.

import turtle as t
no=4

def drawit(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range(no):
        t.fd(50)
        t.lt(360/no)
    t.end_fill()

def redc():
    t.color("red")

def greenc():
    t.color("green")

def bluec():
    t.color("blue")

def set_3():
    global no
    no = 3

def set_4():
    global no
    no = 4

def set_5():
    global no
    no = 5

t.onscreenclick(drawit)
t.onkey(redc, "r")
t.onkey(greenc, "g")
t.onkey(bluec, "b")
t.onkey(set_3, "3")
t.onkey(set_4, "4")
t.onkey(set_5, "5")
t.listen()
t.mainloop()