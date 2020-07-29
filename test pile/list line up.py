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