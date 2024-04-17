import turtle as t

t.shape("turtle")
t.color("blue")

len=t.numinput("","사각형을 그릴 길이를 입력하세요.")
for i in range(4):
    t.fd(len)
    t.lt(90)