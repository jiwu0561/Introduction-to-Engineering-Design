def calculateGrade(mid,final):
    if mid>=0 and final>=0:
        score=(mid+final)/2
        if score >=90:
            grade="A"
        elif score >=80:
            grade="B"
        elif score >=70:
            grade="C"
        elif score >=60:
            grade="D"
        else:
            grade="F"
    else:
        print("점수가 음수입니다.")
        return
    return grade

print("중간:",70,", 기말:",80,", 학점:",calculateGrade(70,80))
score=[[80,90],[65,60],[92,90],[72,-76],[46,58]]
for m,f in score:
    grade=calculateGrade(m,f)
    if grade:
        print("중간:",m,", 기말:",f,", 학점:",grade)