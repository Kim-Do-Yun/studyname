price_list = [32100, 32150, 32000, 32500]
for i in range(0,4,1):
    print(price_list[i])

price_list = [32100, 32150, 32000, 32500]
for i in range(0,4,1):
    print(i,price_list[i])

price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print((len(price_list)-1)-i,price_list[i])

price_list = [32100, 32150, 32000, 32500]
for i in range(1,4,1):
    print(90+ 10*i,price_list[i])

my_list = ["가", "나", "다", "라"]
for i in range(0,len(my_list)-1,1):
    print(my_list[i],my_list[i+1])

my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1,0,-1):
    print(my_list[i],my_list[i-1])

my_list = [100, 200, 400, 800]
for i in range(0,len(my_list)-1,1):
  print(my_list[i+1] - my_list[i])

my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(1,len(my_list)-1,1):
    print( (my_list[i-1] + my_list[i] + my_list[i+1]) / 3 )

low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(0,len(low_prices)-1,1):
    변동폭 = high_prices[i]-low_prices[i]
    volatility.append(변동폭)
print(volatility)