num = int(input('점수를 입력하세요(0-100) --> '))
if num < 0 or num > 100:
    print('0 ~ 100 사이 올바른 점수가 아닙니다.')
if 0 < num < 60:
    print('점수가 {}점이라 "불합격"입니다.'.format(num))
if 100 >= num >= 60:
    print('점수가 {}점이라 "합격"입니다.'.format(num))