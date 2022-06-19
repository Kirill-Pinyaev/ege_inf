from itertools import product


s = '01234'
data = list(product('124', s, s, s, s, s, '0134'))
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