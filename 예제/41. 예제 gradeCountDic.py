학점=['B+','C','A+','B','A+','B+','A']
등급={}
학점.sort()

print("* 학점 리스트:", 학점)
print("* 학점 카운트")
for gr in 학점:
    if gr not in 등급:
        등급[gr]=학점.count(gr)
        print(" %-3s: %d" %(gr,등급[gr]))

print("* 등급 딕셔너리:", 등급)