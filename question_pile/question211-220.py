def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")

def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)

def print_with_smile(string):
    print( string + ":D")

print_with_smile("안녕하세요")

def print_upper_price(price):
    print(price*1.3)
price = int(input("현재 가격:"))
print_upper_price(price)

def print_sum(a,b):
    print(a + b)

def print_arithmetic_operation(a,b):
    print(a, "+",b,"=",a+b)
    print(a, "-",b,"=",a-b)
    print(a, "*",b,"=",a*b)
    print(a, "/",b,"=",a/b)

def print_max(a,b,c):
    max_val = 0
    if a > max_val:
        max_val = a
    elif b > max_val:
        max_val = b
    elif c > max_val:
        max_val = c
    print(max_val) 