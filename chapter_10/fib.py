def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fib(x - 1) + fib(x - 2)

def fib_iterative(x):
    if x < 2:
        return x
    f, g = 0, 1
    for i in range(x - 1):
        f, g = g, g + f
    return g
