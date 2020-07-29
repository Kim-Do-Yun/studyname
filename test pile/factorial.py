a = int(input("시작 수 : "))
b = int(input("끝 수 : "))
c = int(input("증가 값 : "))
print("=======================")

add = 0
mul = 1

print("합 : ", end="")
for i in range(a,b+1,c):
    print(i, end=" + ")
    add += i
print("\b\b", end="= ")
print(add)

print("곱 : ", end="")
for i in range(a,b+1,c):
    print(i, end=" * ")
    mul *= i
print("\b\b", end="= ")
print(mul)