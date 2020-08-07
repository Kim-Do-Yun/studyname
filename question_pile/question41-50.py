ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)

ticker = "BTC_KRW"
ticker1 = ticker.lower()
print(ticker1)

insa = "hello"
insa = insa.capitalize()
print(insa)

file_name = "보고서.xlsx"
a = file_name.endswith('xlsx')
print(a)

file_name = "보고서.xlsx"
a = file_name.endswith(('xlsx','xls'))
print(a)

file_name = "2020_보고서.xlsx"
a = file_name.startswith('2020')
print(a)

a = "hello world"
b = a.split()
print(b)

ticker = "btc_krw"
ticker1 = ticker1.split("_")
print(ticker1)

date = "2020-05-01"
a = date.split("-")
print(a)

data = "039490     "
data = date.rstrip()
print(data)