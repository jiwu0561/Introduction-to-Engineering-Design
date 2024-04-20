# p.142 3.

import random as r
n=r.randint(0,3)
lista = ["6 * 14","7 * 23","15 * 5","24 * 3"]
ans = 0

while ans != eval(lista[n]):
    ans = int(input(f"{lista[n]} = "))

print("맞았습니다.")