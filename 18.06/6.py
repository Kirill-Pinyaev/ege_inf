from itertools import product


s = 'ВОРБЕЙ'
data = list(product('ВОРБЕ', s, s, s, 'ВОРБЕ'))
data = [i for i in data if i.count('Й') <= 1 and (''.join(i).count('ЕЙ') + ''.join(i).count('ЙЕ')) == 0]
print(len(data))