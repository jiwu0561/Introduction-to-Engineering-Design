숫자1 = int(input("숫자를 입력하세요 --> "))
숫자2 = int(input("숫자를 입력하세요 --> "))
나눗셈 = 숫자1/숫자2
print("두 정수: {:3d}, {:3d}".format(숫자1, 숫자2))
print("나눗셈: {}".format(나눗셈))

print("{} / {} = {:5.1f}".format(숫자1, 숫자2, 나눗셈))