def func(x, y):
    if x == 0:
        return y
    return func(x - 1, x + y)


res = func(4, 3)
print(res)
