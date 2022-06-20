with open('17-336.txt') as f:
    data = list(map(int, f.readlines()))
    m = max([i for i in data if i % 37 == 0])
    sp = []
    for i in range(len(data) - 1):
        if data[i] % m == 0 or data[i + 1] % m == 0:
            if (data[i] + data[i + 1]) % m >= 30:
                sp.append(data[i] + data[i + 1])
print(len(sp))
print(min(sp))