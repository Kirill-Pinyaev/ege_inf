s = 3 * 5 ** 1984 - 7 * 25 ** 777 - 11 * 125 ** 666 - 404
data = [0] * 5
while s:
    data[abs(s) % 5] += 1
    s //= 5
print(data[2])