# p.105 2.

x=int(input("첫 번째 숫자를 입력하세요 --> "))
y=int(input("두 번째 숫자를 입력하세요 --> "))

print(f'{x} {y} 의 평균: {(x+y)/2}')

if x > y:
    max = x
    min_ = y
else:
    max = y
    min_ = x

print(f'{x} {y} 중 큰 수: {max}')
print(f'{x} {y} 중 작은 수: {min_}')
