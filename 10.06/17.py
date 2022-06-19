with open('17_0205.txt') as f:
    data = list(map(int, f.readlines()))
    maxx = max([i for i in data if i % 19 == 0])
    sp = []
    for i in range(len(data) - 1):
        if 9 < data[i] < 100 or 9 < data[i + 1] < 100:
            if (data[i] + data[i + 1]) <= maxx:
                sp.append(data[i] + data[i + 1])
    print(len(sp))
    print(max(sp))