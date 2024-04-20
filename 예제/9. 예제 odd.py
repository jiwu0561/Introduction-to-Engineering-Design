num = int(input('정수를 입력하세요 --> '))
if num > 0:
    if num%2:
        print('{}은 홀수입니다.'.format(num))
    else:
        print('{}은 짝수입니다.'.format(num))
else:
    print("정수 값 중 양수로 입력합니다.")