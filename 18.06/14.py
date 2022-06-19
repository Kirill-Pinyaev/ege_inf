with open('17_0205.txt') as f:
    data = list(map(int, f.readlines()))
    sred = sum(data) // len(data)
    sp = []
    for i in range(len(data) - 1):
        if data[i] > sred or data[i + 1] > sred:
            if (data[i] + data[i + 1]) % 7 == 0:
                sp.append(data[i] + data[i + 1])
print(len(sp))
print(min(sp))