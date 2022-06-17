with open('17.txt') as f:
    data = list(map(int, f.readlines()))
    maxx = max([i for i in data if abs(i) % 100 == 13])
    sp = []
    for i in range(len(data) - 1):
        if abs(data[i]) % 100 == 13 or abs(data[i + 1]) % 100 == 13:
            if abs(data[i] - data[i + 1])>= maxx:
                sp.append(data[i] + data[i + 1])
print(len(sp))
print(max(sp))