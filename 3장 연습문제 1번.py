# p.105 1.

number = int(input("정수를 입력하세요 --> "))

total = 0
total = total + number % 10
number = number // 10
total = total + number % 10
number = number // 10
total = total + number % 10
number = number // 10
total = total + number % 10
number = number // 10
total = total + number % 10
number = number // 10

print(f'12345 자리수의 합: {total}')