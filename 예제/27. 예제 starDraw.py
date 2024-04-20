import turtle as t
import random as r

t.color("blue")
xyList=[[0,0],[100,100],[-100,100],[100,-100],[-100,-100]]

for x,y in xyList:
    leng=r.randint(30,100)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    for i in range(5):
        t.fd(leng)
        t.lt(144)
    t.end_fill()

t.mainloop()