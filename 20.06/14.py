def f(n):
    if n == 8:
        return 1
    elif n > 8:
        return 0
    else:
        return f(n + 1) + f(n + 2) + f(n * 3)


a = f(4)
print(a)


def f(n):
    if n == 23:
        return 1
    elif n == 11 or n == 18 or n > 23:
        return 0
    else:
        return f(n + 1) + f(n + 2) + f(n * 3)


b = f(8)
print(b)
print(a * b)
