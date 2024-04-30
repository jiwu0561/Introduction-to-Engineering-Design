학점=[]
while True:
    등급=input("학점을 입럭하세요 --> ")
    if 등급=="s" or 등급=="S":
        break
    elif 등급 in ['A+','A','B+','B','C+','C','D+','D','F']:
        학점.append(등급)
    else:
        print("올바른 학점을 입력하세요!")
print("* 학점 리스트:", 학점)
if "F" in 학점:
    print("F:",학점.count("F"))
else:
    print("F 학점은 없습니다.")