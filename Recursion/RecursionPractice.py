def fun1(n):
    if n == 0:
        return
    print(n)
    fun1(n - 1)
    print(n)


fun1(3)

print()


# ********************************************************************************************

def fun2(n):
    if n <= 1:
        return 0
    else:
        return 1 + fun2(n // 2)


res = fun2(16)
print(res)

# It returns (log2 N) i.e log2 16 = 4

print()
# *********************************************************************************************


# def fun3(n):
