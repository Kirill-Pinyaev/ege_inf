from math import ceil

with open('27_1.txt') as f:
    data = []
    for i in f:
        data.append(list(map(int, i.split())))
    n = 7
    for i in data:
        i[1] = ceil(i[1] / 156)
    sp = []
    print(data)
    for i in data:
        count = 0
        for j in data:
            if i[0] != j[0]:
                count += abs(i[0] -j[0]) * j[1]
        sp.append((i[0], count))
    sp = sorted(sp, key=lambda x: x[1])
    print(*sp[0])
