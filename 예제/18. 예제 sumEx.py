n=int(input("양수를 입력하세요 --> "))
hap=0
if n>=1:
    for i in range(1, n+1):
        hap+=i
    print("1부터",n,"까지의 합계는",hap,"이다.")
else:
    print("입력은 양수로 하세요.")