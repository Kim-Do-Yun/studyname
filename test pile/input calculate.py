a = int(input("정수를 입력하시오 : "))

'''
b = a//1000
c = (a%1000)//100
d = ((a%1000)%100)//10
e = (((a%1000)%100)%10)
x = b + c + d + e
'''

result = 0

result += a // 1000             # 1
a = a % 1000                    # 234

result += a // 100              # 2
a = a % 100                     # 34

result += a // 10               # 3
result +=  a % 10               # 4

print(F"자리수의 합 : {result}")

# Chapter 3 - 7번

import time

print(time.time())