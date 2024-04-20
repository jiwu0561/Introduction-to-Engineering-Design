hap=0

while True:
    score=float(input("점수를 입력하세요 --> "))
    if score <= 0:
        break
    elif score < 70:
        continue
    hap += score
print("70이상인 점수의 합계:",hap)