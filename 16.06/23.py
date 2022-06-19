def f(n):
    if n == 43:
        return 1
    elif n < 43:
        return 0
    else:
        return f(n - 8) + f(n // 2)
a = f(102)
def f(n):
    if n == 5:
        return 1
    elif n < 5:
        return 0
    else:
        return f(n - 8) + f(n // 2)
b = f(43)
print(a, b)
print(a * b)