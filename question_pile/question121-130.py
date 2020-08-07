word = input("문자를 입력하시오: ")
if word.islower() == True:
    print(word.upper())
else:
    print(word.lower())

score = int(input("score: "))
if 81 <= score <= 100:
    print("grade is A")
elif 61 <= score <= 80:
    print("grade is B")
elif 41 <= score <= 60:
    print("grade is C")
elif 21 <= score <= 40:
    print("grade is D")
else:
    print("grade is E")

환율 = { "달러": 1167, "엔":1.096, "유로": 1268, "위안": 171}
user = input("입력(숫자와 글자를 공백을 두고 쓰기): ")
num, currency = user.split()
print(float(num)*환율[currency], "원")

a = int(input("input number1: "))
b = int(input("input number2: "))
c = int(input("input number3: "))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

number = input("휴대전화 번호 입력: ")
num = number.split("-")[0]
if num == "011":
    com = "SKT"
elif num == "016":
    com = "KT"
elif num == "019":
    com = "LGU"
else:
    com = "알수없음"
print("당신은", com ,"사용자입니다.")

number = input("우편번호(5자리): ")
dnumber = number[:3]
if dnumber in ["010", "011", "012"]:
    print("강북구")
elif dnumber in ["013", "014", "015"]:
    print("도봉구")
elif dnumber in ["016", "017", "018", "019"]:
    print("노원구")

주민등록번호 = input("주민등록번호: ")
성별 = 주민등록번호[-7]
if 성별 in ["1","3"]:
    print("남자")
elif 성별 in ["2","4"]:
    print("여자")
'''
주민번호 = input("주민등록번호: ")
주민번호 = 주민번호.split("-")[1]
if 주민번호[0] == "1" or 주민번호[0] == "3":
    print("남자")
else:
    print("여자")
'''

주민등록번호 = input("주민등록번호: ")
성별 = 주민등록번호[-7:]
if 0 <= int(성별[1:2]) <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")

num = input("주민등록번호: ")
계산 = int(num[0])*2 +int(num[1])*3 +int(num[2])*4 +int(num[3])*5 +int(num[4])*6 +int(num[5])*7 +int(num[7])*8 +int(num[8])*9 +int(num[9])*2 +int(num[10])*3 +int(num[11])*4 +int(num[12])*5
if str(11-계산%11) == num[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
변동폭 = float(btc["max_price"])-float(btc["min_price"])
시가 = flaot(btc["opening_price"])
최고가 = float(btc["max_price"])
if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")

