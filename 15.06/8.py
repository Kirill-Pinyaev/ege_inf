from itertools import product


s = 'ОБЩЕСТВ'
data = list(product('ОБЕСТ', s, s, 'В', 'В'))
data = [i for i in data if ((''.join(i).count('ЕВ') + ''.join(i).count('ВЕ')) == 0) and (''.join(i).count('ТБ') >= 1)]
print(len(data))