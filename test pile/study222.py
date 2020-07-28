a = []

for i in range(1,11,1):
    b = int(input(str(i) + "번째 숫자를 입력하시오 : "))
    a.append(b)

print("입력된 값은",a,"이며,")

for i in range(9): # 0~9
    if a[i] > a[i+1]: # 10
        temp = a[i]
        a[i] = a[i+1]
        a[i+1] = temp
print("제일 큰 값은",a[i+1],"이고,")

for i in range(9):
    if a[i] < a[i+1]:
        temp = a[i]
        a[i] = a[i+1]
        a[i+1] = temp
print("제일 작은 값은",a[i+1],"이다.")


# 참고
max_num = 0         # 9
num_list = []       # 2 4 3 5 1 6 8 9 0

for i in range(10) :
    num = int(input(str(i + 1) + "번째 숫자를 입력하시오 >> "))
    num_list.append(num)

    if num > max_num :
        max_num = num

min_num = max_num

for i in range(10) :
    if num_list[i] < min_num :
        min_num = num_list[i]

print("입력된 값은 " + str(num_list) + "이며,")
print("제일 큰 값은 " + str(max_num) + "이고,")
print("제일 작은 값은 " + str(min_num) + "이다.")