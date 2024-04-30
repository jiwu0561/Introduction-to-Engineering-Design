공연1={"kim","lee","han","cho","park"}
공연2={"lee","han","jung","cho","choi"}

print("* 공연1 참석자:", end=" ")
for 사람 in 공연1:
    print(사람, end=" ")

print("\n* 공연2 참석자:", end=" ")
for 사람 in 공연2:
    print(사람, end=" ")

print("\n* 두 공연 모두 참석한 사람:", end=" ")
공연= 공연1.intersection(공연2)
for 사람 in 공연:
    print(사람,end=" ")