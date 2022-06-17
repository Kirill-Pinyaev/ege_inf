def f(n):
    if n == 18:
        return 1
    elif n == 20 or n < 18:
        return 0
    else:
        return f(n - 1) + f(n - 2) + f(n ** 0.5)
a = f(27)
print(a)
def f(n):
    if n == 6:
        return 1
    elif n < 6:
        return 0
    else:
        return f(n - 1) + f(n - 2) + f(n ** 0.5)
b = f(18)
print(b)
print(a * b)