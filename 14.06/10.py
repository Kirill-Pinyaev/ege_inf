def f(n):
    if n == 10:
        return 1
    elif n == 15 or n < 10:
        return 0
    else:
        return f(n - 1) + f(n - 3)
a = f(22)
print(a)
def f(n):
    if n == 2:
        return 1
    elif n < 2:
        return 0
    else:
        return f(n - 1) + f(n - 3)
b = f(10)
print(b)
print(a * b)