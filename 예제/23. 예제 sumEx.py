hap=0; count=0
while True:
    num=float(input("숫자를 입력하세요 --> "))
    if num <= 0:
        break
    hap += num
    count += 1
avg = hap/count
print("합계:",hap,"평균:",avg)