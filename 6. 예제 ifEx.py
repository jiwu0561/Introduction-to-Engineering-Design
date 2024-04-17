num = int(input('정수를 입력하세요 --> '))
if num < 0:
    print('{}은 음수입니다.'.format(num))
if num == 0:
    print('{}은 "Zero"입니다.'.format(num))
if num > 0:
    print('{}은 양수입니다.'.format(num))