a = input("파일 이름을 입력하세요 : ")
num = 0
infile = open(a, "r")           # a / "a" == 'a'
for line in infile:
    line = line.rstrip()
    word_line = line.split()
    for word in word_line:
        b = len(word)
    num += b

print("파일 안에는 총", num,"개의 글자가 있습니다.")
infile.close()