import turtle as t
import random as r
t.shape("turtle")
t.color("blue")
n = t.numinput("","도형을 그릴 숫자를 입력하시오. 0(원), 3(삼각형), 4(사각형)")

if n == 0 or 3<=n<=4:
    l = r.randint(70, 100)
    if n==4:
        for i in range(4):
            t.fd(l)
            t.lt(90)
    elif n==3:
        for i in range(3):
            t.fd(l)
            t.lt(120)
    elif n==0:
        t.circle(l)
else:
    t.ht()
    t.write("올바른 숫자를 입력하세요.")

t.mainloop()