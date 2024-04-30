딕셔너리={1:"컴퓨터공학과", 2:"소프트웨어공학과", 3:"전자공학과"}

while True:
    code=int(input("학과 코드를 입력하세요 (1-3), 끝낼 경우(0) --> "))
    if code==0:
        break
    elif 1 <= code <= 3:
        print("학과 코드 : %d, 학과 이름 : %s" %(code, 딕셔너리[code]))
    else:
        print("올바른 학과 코드를 입력하세요.")