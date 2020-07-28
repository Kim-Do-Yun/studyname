

for i in range(5):
    for j in range(5-i):
        print(" ", end="")
    for d in range((2*i)+1):
        print("*", end="")
    print()
for i in range(5):
    for j in range(i+1):
        print(" ", end="")
    for d in range(10-((i*2)+1)):
        print("*", end="")
    print()
    
