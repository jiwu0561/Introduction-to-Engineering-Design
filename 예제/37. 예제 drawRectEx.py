import turtle as t
import random as r
t.shape("turtle")
d_list=[[0,0,"red"],[100,100,"green"],[-100,100,"blue"],[200,150,"yellow"],[-200,100,"pink"]]

def drawRect(x,y,c):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(c)
    leng = r.randint(50,100)
    t.begin_fill()
    for i in range(4):
        t.fd(leng)
        t.lt(90)
    t.end_fill()

for x,y,c in d_list:
    drawRect(x,y,c)

t.mainloop()