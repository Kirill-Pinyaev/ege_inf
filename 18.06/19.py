def f(n):
    if n == 11:
        return 1
    elif n > 11:
        return 0
    else:
        return f(n + 1) + f(n + 2) + f(n * 3)
a = f(5)
print(a)
def f(n):
    if n == 26:
        return 1
    elif n == 13 or n == 15 or n > 26:
        return 0
    else:
        return f(n + 1) + f(n + 2) + f(n * 3)
b = f(11)
print(a * b)