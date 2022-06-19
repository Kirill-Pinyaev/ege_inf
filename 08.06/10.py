with open('26_0806.txt') as f:
    data = list(map(int, f.readlines()))
    n, k, m = 600, 60, 240
    data = sorted(data, reverse=True)
    print(data[k - 1])
    print(data[m + k - 1])
