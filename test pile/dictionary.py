book = {}           # 빈 딕셔너리
book["홍길동"] = "010-1234-5678"
book["이순신"] = "010-1234-5679"
book["강감찬"] = "010-1234-5670"
book["김철수"] = "010-1234-5678"

for key in book.keys() :
    print(key, book[key])

for value in book.values() :
    print(value)

for key, value in book.items() :
    if value == "010-1234-5678" :
        print(key)