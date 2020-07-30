a = "3"
b = "4"
print(a+b)

print("Hi"*3)

print('-'*80)

t1 = 'python'
t2 = 'java'
t3 = t1+' '+t2+' '
print(t3*4)

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" %(name1, age1))
print("이름: %s 나이: %d" %(name2, age2))

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}" .format(name1, age1))
print("이름: {} 나이: {}" .format(name2, age2))

상장주식수 = "5,969,782,550"
a = 상장주식수.replace(',','')
b = int(a)
print(b,type(b))

분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

data = "   삼성전자   "
data1 = data.strip()
print(data1)