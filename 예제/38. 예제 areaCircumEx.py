def areaCircum():
    return (PI*r**2, 2*PI*r)

PI = 3.14
n = int(input("원의 수 입력 --> "))
for i in range(n):
    r = float(input("반지름 입력 --> "))
    (area, circum)= areaCircum()
    print("반지름",r,"인 원의 면적 :",area,", 둘레 :",circum)