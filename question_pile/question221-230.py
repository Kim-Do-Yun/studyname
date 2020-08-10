def print_reverse(string):
    print(string[::-1])
print_reverse("python")

def print_score(score_list):
    print(sum(score_list)/len(score_list))
print_score([1,2,3])

def print_even(even_list):
    for i in even_list:
        if i%2 == 0:
            print(i)

def print_keys(dic):
    for keys in dic.keys():
        print(keys)

def print_value_by_key(dic,key):
    print(dic[key])
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
print_value_by_key(my_dict,"10/26")

def print_5xn(line):
    num = int(len(line)/5)
    for i in range(num+1):
        print(line[i*5:i*5+5])

def print_mxn(line,num):
    number = int(len(line)/num)
    for i in range(number+1):
        print(line[i*num:i*num+num])

def calc_monthly_salary(mon):
    money = int(mon/12)
    return money

def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)

def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)