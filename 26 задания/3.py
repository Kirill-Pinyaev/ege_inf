with open('26_3.txt') as f:
    data = list(map(int, f.readlines()))
    n = data.pop(0)
    maxsum = 0
    sp = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            # print(i, j)
            print(data[i:j])
            sp.append((i + 1, j, sum(data[i:j])))
sp = sorted(sp, key=lambda x: (-x[2], -x[0], x[1]))
print(sp[0][0], sp[0][1])
