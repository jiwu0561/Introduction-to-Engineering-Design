n=int(input("양수를 입력하세요 --> "))
fac=1
if n<=1:
    for i in range(1, n+1):
        fac *= i
    print(n,"! 은",fac,"이다.")
else:
    print("입력은 양수로 하세요.")