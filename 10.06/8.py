from itertools import product


s = 'ЖУРАВЛЬ'
data = list(product('ЖУРАВЛ', s, s, s, s))
data = [i for i in data if i.count('Ж') <= 2 and i.count('У') == 0]
print(len(data))