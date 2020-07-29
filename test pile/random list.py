import random

num_list = [0, 0, 0, 0, 0, 0]


for _ in range(1,1001,1):
    a = random.randint(1,6)
    '''
    if a == 1:
        num_list[0] += 1
    if a == 2:
        num_list[1] += 1
    if a == 3:
        num_list[2] += 1
    if a == 4:
        num_list[3] += 1
    if a == 5:
        num_list[4] += 1
    if a == 6:
        num_list[5] += 1
    '''
    num_list[a-1] += 1
    
for i in range(6) :
    print(i+1, "인 경우 ", num_list[i])