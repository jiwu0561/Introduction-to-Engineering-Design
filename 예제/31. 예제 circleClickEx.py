import turtle as t
t.shape("turtle")
def draw(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("blue")
    t.circle(20)
    t.end_fill()

t.onscreenclick(draw)
t.mainloop()