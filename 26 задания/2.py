with open('26_2.txt') as f:
    n, g, m = list(map(int, f.readline().split()))
    data = list(map(int, f.readline().split()))
    for i in range(n):
        count = 0
        for k in range(g + 1):
            if i + k > n - 1:
                break
            count += data[i + k]
        if count == m:
            print(i + 1)
