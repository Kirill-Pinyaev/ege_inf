from itertools import product

#м - 1  а - 2 г - 3 н - 5 о - 4 л - 7 и - 6 я - 8
s = '12354768'
data = list(product('2354768', s, s, s, s))
sp = []
for i in data:
    for j in range(len(i) - 1):
        if int(i[j]) % 2 == 0 and int(i[j + 1]) % 2 == 0:
            sp.append(i)
            break
print(len(sp))