s = 256 ** 78 + 2 * 64 ** 77 + 3 * 16 ** 82 - 4 ** 86 -81
data = [0] * 4
while s:
    data[s % 4] += 1
    s //= 4
print(data[3])