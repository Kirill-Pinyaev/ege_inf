with open('17.txt') as f:
    data = list(map(int, f.readlines()))
    maxx = 2 * max([i for i in data if abs(i) % 10 == 7])
    sp = []
    for i in range(len(data) - 1):
        if (abs(data[i]) % 10 == 7 and abs(data[i + 1]) % 10 != 0) or (abs(data[i]) % 10 != 7 and abs(data[i + 1]) % 10 == 0):
            if (data[i] + data[i + 1]) < maxx:
                sp.append(data[i] + data[i + 1])
    print(len(sp))
    print(max(sp))