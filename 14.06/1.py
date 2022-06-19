with open('17_0205.txt') as f:
    data = list(map(int, f.readlines()))
    minn = min([i for i in data if i % 100 == 11])
    sp = []
    for i in range(len(data) - 1):
        if data[i] < minn or data[i + 1] < minn:
            sp.append(data[i] + data[i + 1])
    print(len(sp))
    print(max(sp))
