import random
a = random.randint(1,100)
b = random.randint(1,100)

c = int(input(str(a) + "-" + str(b) + "="))

if a-b==c:
    print("맞았습니다.")
else:
    print("틀렸습니다.")