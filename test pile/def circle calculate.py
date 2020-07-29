r = int(input("반지름의 값을 입력하세요 : "))
pi = 3.1415926

def circleArea(r):
    return pi*r*r
    
def circleCircumference(r) :
    return 2*pi*r
    
print("반지름이", float(r), "인 원의 면적 :", circleArea(r))
print("반지름이", float(r), "인 원의 둘레 :", circleCircumference(r))
