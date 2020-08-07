my_variable = ()
print(type(my_variable))

movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

t = (1,)
print(t)

t = 1,2,3,4
print(type(t))

t = ("a", "b", "c")
t = ("A", "b", "c")
print(t)

interest = ("삼성전자", "LG전자", "SK Hynix")
data = list(interest)
print(data, type(data))

interest = ["삼성전자", "LG전자", "SK Hynix"]
data = tuple(interest)
print(data, type(data))

temp = ('apple', 'banana', 'cake')
a,b,c = temp
print(a,b,c)

data = tuple(range(2,100,2))
print(data)
