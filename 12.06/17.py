with open('17-243.txt') as f:
    data = list(map(int, f.readlines()))
    number = [i for i in data if i % 33 == 0]
    suum = 0
    for i in number:
        for j in str(i):
            suum += int(j)
    sp = []
    for i in range(len(data) - 1):
        if data[i] > suum or data[i + 1] > suum:
            sp.append(data[i] + data[i + 1])
    print(len(sp))
    print(min(sp))
