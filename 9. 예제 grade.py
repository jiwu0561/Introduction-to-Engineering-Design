num = int(input('점수를 입력하세요(0-100) --> '))
if num < 0 or num > 100:
    print('올바른 점수가 아닙니다.')
else:
    if num >= 90:
        grade = 'A'
    elif num >= 80:
        grade = 'B'
    elif num >= 70:
        grade = 'C'
    elif num >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print('성적은 {}점이고, 학점은 "{}"입니다.'.format(num, grade))