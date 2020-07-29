a = int(input("몇개의 수를 입력받을 건가요? "))

s = []

for i in range(1, a + 1, 1):                # C 계열 언어와 달리, python 동적할당
    b = int(input(str(i)+"번째 수 :"))
    s.append(b)

print("입력직후 :", s)

for _ in range(0,len(s),1):
    for i in range(0, len(s)-1, 1) : # i=0;i<size;i++
        if s[i] > s[i+1] :
            temp = s[i]
            s[i] = s[i+1]
            s[i+1] = temp

print("정렬 후 : ", s)