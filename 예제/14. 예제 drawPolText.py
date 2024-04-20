# 도형 그리기 예제2
import turtle as t

t.shape("turtle")
t.color("blue")

n = t.textinput("","도형 이름을 입력하시오. 원, 삼각형, 사각형")
if n=="원" or n=="삼각형" or n=="사각형":
    l = t.numinput("","도형을 그릴 길이(반지름)를 입력하시오.")
    if n=="사각형":
        for i in range(4):
            t.fd(l)
            t.lt(90)
    elif n=="삼각형":
        for i in range(3):
            t.fd(l)
            t.lt(120)
    elif n=="원":
        t.circle(l)
else:
    t.ht()
    t.write("올바른 도형 이름을 입력하세요.")