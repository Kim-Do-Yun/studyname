book = {}

book["파이썬"] = "최근에 가장 떠오르는 프로그래밍 언어"
book["변수"] = "데이터를 저장하는 메모리 공간"
book["함수"] = "작업을 수행하는 문장들의 집합에 이름을 붙인 것"
book["리스트"] = "서로 관련이 없는 항목들의 모임"

print("다음은 어떤 단어에 대한 설명일까요\n")
print("==================================")

for key in book.keys():
    print(book[key],"?")
    
    i = 1
    for probloem in book.keys():
        print(str("(") + str(i) + str(")"), probloem ,end="\t")
        i += 1

    a = input("\n>> ")
    if a == key:
        print("정답입니다!")
    else:
        print("오답입니다.")
 