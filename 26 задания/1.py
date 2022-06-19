with open('26-j8.txt') as f:
    data = list(map(int, f.readlines()))
    n = data.pop(0)
    data = sorted(data)
    n1 = int(n * 0.7)
    sp1 = []
    for i in range(n):
        if i < n1:
            sp1.append(data[i] - (data[i] * 0.3))
        else:
            sp1.append(data[i] - (data[i] * 0.4))
    n2 = int(n / 2)
    sp2 = []
    for i in range(n):
        if i < n2:
            sp2.append(data[i] - (data[i] * 0.4))
        else:
            sp2.append(data[i] - (data[i] * 0.35))
    print(int(abs(sum(sp1) - sum(sp2))))
    print(int(max(max(sp1), max(sp2))))