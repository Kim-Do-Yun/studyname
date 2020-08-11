def make_url(num):
    return "www."+num+".com"
print(make_url("naver"))

def make_list(mlist):
    a = []
    for i in mlist:
        a.append(i)
    return a
print(make_list("abcd"))

def pickup_even(nlist):
    a = []
    for i in nlist:
        if i % 2 == 0:
            a.append(i)
    return a
print(pickup_even([3,4,5,6,7,8]))

def convert_int(num):
    number = int(num.replace(",",""))
    return number
print(convert_int("1,234,567"))

def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)

def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
