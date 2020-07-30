letters = 'python'
print(letters[0], letters[2])

license_plate = "24가 2210"
print(license_plate[-4:])

string = "홀짝홀짝홀짝"
print(string[::2])

string = "PYTHON"
print(string[::-1])

phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-"," ")
print(phone_number1)

phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-","")
print(phone_number1)

url = "heep://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

string = 'abcdfe2a354a32a'
string1 = string.replace('a', 'A')
print(string1)