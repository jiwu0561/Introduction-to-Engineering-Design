dict = {"하나":"one", "소녀":"girl", "사람":"person", "소년":"boy", "단어":"word", "사과":"apple"}

print("* 사전 목록")
for 키 in dict.keys():
    print(키)
print()

while True:
    word=input("단어를 입력하세요 --> 끝낼 때 (s, S)")
    if word=="s" or word =="S":
        break
    elif word in dict.keys():
        print(dict[word])
    else:
        print("목록에 있는 단어를 입력하세요.")