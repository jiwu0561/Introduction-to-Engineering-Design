import turtle as t
import time as tm

t.shape("turtle")
t.color("blue")
d_list=["사각형","삼각형","원"]

while True:
    s = t.textinput("","도형을 입력하시오: ")
    if s =="s"or"S":
        break
    if s in d_list:
        leng = t.numinput("도형 그리기","길이(반지름) 입력")
        if s == "사각형":
            for i in range(4):
                t.fd(leng)
                t.lt(90)
        elif s == "삼각형":
            for i in range(3):
                t.fd(leng)
                t.lt(120)
        elif s == "원":
            t.circle(leng)
    else:
        t.ht()
        t.write("올바른 도형 이름을 입력하세요.")
    tm.sleep(3)
    t.clear()
    t.st