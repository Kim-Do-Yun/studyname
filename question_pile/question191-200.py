data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for line in data:
    for word in line:
        print(word+word*0.014)

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for line in data:
    for word in line:
        print(word+word*0.014)
    print("----")

result = []
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for line in data:
    for word in line:
        result.append(word+word*0.014)
print(result)

result = []
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for line in data:
    a = []
    for word in line:
        a.append(word+word*0.014)
    result.append(a)
print(result)

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for line in ohlc[1:]:
    print(line[3])

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for line in ohlc[1:]:
    if line[3] > 150:
        print(line[3])

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for line in ohlc[1:]:
    if line[3] >= line[0]:
        print(line[3])

volatility = []
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for line in ohlc[1:]:
    volatility.append(line[1] - line[2])
print(volatility)

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for line in ohlc[1:]:
    if line[0] < line[3]:
        print(line[1] - line[2])
    
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
num = 0
for line in ohlc[1:]:
    a = line[3] - line[0]
    num += a
print(num)