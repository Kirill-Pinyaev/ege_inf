from  itertools import product


s = '012345678'
data = list(product('13578', s, s, s, s, s, s))
data = [i for i in data if ''.join(i)[-1] != ''.join(i)[-2] != ''.join(i)[-3]]
print(len(data))