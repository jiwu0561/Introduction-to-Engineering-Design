# p.213 4.

items = {"자바":5, "파이썬":6, "C++":2, "C":1}
def item_print():
    print("================")
    print("  물품 목록")
    print("================")
    for key in sorted(items.keys()):
        print(" "+key,":",items[key])
    print("================")

while True:
    item_print()
    while True:
        print("책 목록 구매나 보충 선택 --> 구매: 1, 보충: 2, quit: 0 ")
        choice = input("원하는 번호를 선택하세요. --> ")
        if choice == "0" or choice == "1" or choice == "2":
            break
        else:
            continue # 예외 처리
    if choice == "0":
        print("종료합니다...")
        break
    n = int(choice)
    if n==1:
        item = input("구매할 책 이름을 입력하세요: ")
        no = int(input("구매 수량을 입력하세요: "))
        if not item in items or items[item] == 0:
            print("물품이 없습니다.")
            continue
        if items[item] >= no:
            print(item, " --> ", no, "개 구매함...")
            items[item] -= no
            continue
        else:
            print(item, " --> 재고량이 부족해서", items[item], "개만 구매함...")
            items[item] = 0
            continue
    elif n==2:
        item = input("보충할 책 이름을 입력하시오: ")
        if not item in items:
            continue # 예외 처리
        no = int(input("보충 수량을 입력하세요: "))
        items[item] += no
        continue