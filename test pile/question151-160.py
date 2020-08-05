리스트 = [3, -20, -3, 44]

for i in 리스트:
    if i < 0:
        print(i)

리스트 = [3,100,23,44]
for 변수 in 리스트:
    if 변수%3 == 0:
        print(변수)

리스트 = [13, 21, 12, 14, 30, 18]
for 변수 in 리스트 :
    if 변수 < 20 and 변수%3 == 0:
        print(변수)

리스트 = ["I", "study", "python", "language", "!"]
for 변수 in 리스트:
    if len(변수) >= 3:
        print(변수)

리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
    if 변수.isupper() == True:
        print(변수)

리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
    if 변수.islower() == True:
        print(변수)

리스트 = ['dog', 'cat', 'parrot']
for 변수 in 리스트:
    if 변수.islower() == True:
        print(변수.capitalize())

리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for 변수 in 리스트:
    변수 = 변수.split(".")
    print(변수[0])

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
    word = 변수[-1]
    if word == 'h':
        print(변수)

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
    word = 변수[-1]
    if word == 'h' or word == 'c':
        print(변수)