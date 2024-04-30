import turtle as t
def draw(x,y):
    t.goto(x,y)
def redc():
    t.color("red")
def bluec():
    t.color("blue")
def greenc():
    t.color("green")
t.shape("turtle")
t.pensize(5)

t.onscreenclick(draw)

t.onkey(t.penup, "Up")
t.onkey(t.pendown, "Down")
t.onkey(redc, "r")
t.onkey(bluec, "b")
t.onkey(greenc, "g")
t.listen()
t.mainloop()