import random

while True:
    a = random.randint(1,9)
    b = random.randint(1,9)
    num = int(input(str(a)+"*"+str(b)+"는" ))

    if a*b == num :
        print("맞았습니다.")
        break

