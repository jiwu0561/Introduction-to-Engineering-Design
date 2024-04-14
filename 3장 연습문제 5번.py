# p.107 5.

price = int(input("물건 값을 입력하세요 --> "))
money = int(input("투입한 돈을 입력하세요 --> "))

change = money-price
print("거스름돈:", change)

coin500s = change // 500
change500s = change % 500
print("500원 동전의 개수:", coin500s)

if change500s != 0:
    coin100s = change500s // 100
    change100s = change500s % 100
    print("100원 동전의 개수:", coin100s)

if change100s != 0:
    coin50s = change100s // 50
    change50s = change100s % 50
    print("50원 동전의 개수:", coin50s)

if change50s != 0:
    coin10s = change50s // 10
    print("10원 동전의 개수:", coin10s)

