학점=['B+','C','A+','B','A+','B+','A']
check=[]
학점.sort()
print("* 학점 리스트:",학점)
print("* 학점 카운트")
for gr in 학점:
    if gr not in check:
        check.append(gr)
        count=학점.count(gr)
        print(" %-3s: %d"%(gr,count))