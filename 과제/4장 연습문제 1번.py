# p.141 1.

start = int(input("구구단의 시작 단을 입력하세요 --> "))
end = int(input("구구단의 끝 단을 입력하세요 --> "))

for i in range(start, end+1):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j:2}", end=" ")
    print("")