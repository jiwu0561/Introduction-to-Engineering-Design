import datetime

now=datetime.datetime.now()
print("현지 날짜와 시간 :", now)

print("{}년 {}월 {}일 {}시".format(now.year,now.month,now.day,now.hour))