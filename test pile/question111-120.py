insa = "안녕하세요"
print(insa*2)

a = int(input("숫자를 입력하세요: "))
print(a+10)

a = int(input("숫자를 입력하세요:"))
if a%2 == 0:
    print("짝수")
else:
    print("홀수")

a = int(input("입력값:"))
num = a+20
if num > 255:
    print("출력값:",255)
else:
    print("출력값:",num)


a = int(input("입력값:"))
num = a-20
if num > 255:
    print("출력값:",255)
elif num < 0:
    print("출력값:",0)
else:
    print("출력값:",num)

time = input("현재시간(ex 00:00): ")
if time[-2:] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")

fruit = ["사과", "포도", "홍시"]
a = input("좋아하는 과일은? ")
if a in fruit :
    print("정답입니다.")
else:
    print("오답입니다.")

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
종목 = input("종목명을 입력하시오: ")
if 종목 in warn_investment_list :
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
key = input("제가 좋아하는 계절은: ")
if key in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
val = input("제가 좋아하는 과일은: ")
if val in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")
