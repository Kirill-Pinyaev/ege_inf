with open('26_180622.txt') as f:
    data = []
    for i in f:
        data.append(list(map(int, i.split())))
    n, m = data.pop(0)
    data = sorted(data, key=lambda x: (x[0], -x[1], x[2]))
    sp = []
    for i in range(n - 1):
        if data[i][1] == data[i + 1][1] and data[i][0] == data[i][0]:
            if data[i][2] == 1 and data[i + 1][2] == 6:
                sp.append(data[i][1])
    print(max(sp))
    print(len(sp))


