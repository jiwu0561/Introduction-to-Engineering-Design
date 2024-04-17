import datetime as dt
now=dt.datetime.now()
print("현재 날짜와 시간 :", now)

if 3<=now.month<=5:
    print("현재 {}월 : 봄입니다.".format(now.month))
elif 6<=now.month<=8:
    print("현재 {}월 : 여름입니다.".format(now.month))
elif 9<=now.month<=11:
    print("현재 {}월 : 가을입니다.".format(now.month))
else:
    print("현재 {}월 : 겨울입니다.".format(now.month))