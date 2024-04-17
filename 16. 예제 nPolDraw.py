import turtle as t

t.shape("turtle")
t.color("blue")

n=int(t.numinput("","몇각형을 그릴까요?"))

leng=t.numinput("",str(n)+"각형의 길이를 입력하세요.")
for i in range(n):
    t.forward(leng)
    t.left(360/n)