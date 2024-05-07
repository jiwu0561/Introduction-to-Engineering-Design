dict = {"가화만사성":"家和萬事成 가정이 화목하면 모든 일이 잘 이루어짐",
        "갑론을박":"甲論乙駁 자기의 주장을 세우고 남의 주장을 반박함",
        "과대망상":"誇大妄想 턱없이 과장하여 그것을 믿는 망령된 생각",
        "대서특필":"大書特筆 특히 드러나게 큰 글자로 적어 표시함",
        "동병상련":"同病相憐 같은 처지에 있는 사람끼리 서로 동정함",
        "외유내강":"外柔內剛 겉으로 보기에는 부드러우나 속은 꿋꿋하고 강함"}

print("* 고사성어 목록")
for 키 in dict.keys():
    print(키)
print()

while True:
    gosa = input("고사성어를 입력하세요 --> 끝낼 때(s, S)")
    if gosa=="s" or gosa=="S":
        break
    elif gosa in dict.keys():
        print(dict[gosa])
    else:
        print("목록에 있는 고사성어를 입력하세요.")