a = input("입력 파일 이름 : ")
b = input("출력 파일 이름 : ")
infile = open(a, "r", encoding= "UTF-8")
content = infile.read()
outfile = open(b, "w")
outfile.write(content)

infile.close()
outfile.close()
