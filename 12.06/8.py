from itertools import product


s = '012345'
data = list(product('24', s, s, s, s, s, s))
data = [i for i in data if i.count('4') <= 1]
print(len(data))