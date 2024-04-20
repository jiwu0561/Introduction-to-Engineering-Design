# p.107 6.

import turtle as t

color1 = input("첫번째 색상을 입력하세요. --> ")
color2 = input("두번째 색상을 입력하세요. --> ")
color3 = input("세번째 색상을 입력하세요. --> ")

t.shape("turtle")
t.fillcolor(color1)
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(100, 0)
t.down()

t.fillcolor(color2)
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(200, 0)
t.down()

t.fillcolor(color3)
t.begin_fill()
t.circle(50)
t.end_fill()

t.mainloop()