code = int(input("학과 코드를 입력하세요 (1-3) --> "))

if code==1:
    print("학과 코드:",code,"학과 이름 : 컴퓨터공학과")
if code==2:
    print("학과 코드:",code,"학과 이름 : 소프트웨어공학과")
if code==3:
    print("학과 코드:",code,"학과 이름 : 전자공학과")
if code<1 or code>3:
    print("올바른 학과 코드를 입력하세요")