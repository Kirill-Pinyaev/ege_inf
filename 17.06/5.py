from itertools import product


s = '0123456'
data = list(product('1246', s, s, s, s, '01356'))
data = [i for i in data if i.count('6') <= 1]
print(len(data))
sp = []
for i in data:
    a = ''.join(i)
    flag = True
    for j in range(len(a) - 1):
        if int(a[j]) % 2 == 0 and int(a[j + 1]) % 2 == 0:
            flag = False
    if flag:
        sp.append(a)
print(len(sp))