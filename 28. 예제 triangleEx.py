import turtle as t
t.shape("turtle")
t.color("blue")

def triangle(length):
    for i in range(3):
        t.fd(length)
        t.lt(120)

triangle(100)

t.up()
t.goto(-150, 0)
t.down()
triangle(80)

t.up()
t.goto(150, 0)
t.down()
triangle(120)
