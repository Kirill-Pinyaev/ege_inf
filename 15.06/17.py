def g(a, b):
    a = str(a)
    b = str(b)
    if a[-1] == b[-1]:
        return True
    return False


with open('17-335.txt') as f:
    data = list(map(int, f.readlines()))
    m = min([i for i in data if i % 43 == 0])
    sp = []
    sp2 = []
    for i in range(len(data) - 1):
        if ((data[i] + data[i + 1]) % m == 0) or (g(data[i], m) or g(data[i + 1], m)):
            sp.append(data[i])
            sp2.append(data[i])
            sp2.append(data[i + 1])
print(len(sp))
print(max(sp2))