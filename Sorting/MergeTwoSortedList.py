# write a python program to merge two sorted lists and return a single list

# Solution 1: Naive approach

def merge(a, b):
    res = a + b
    res.sort()
    return res


a = [10, 15, 30]
b = [2, 20]
print(merge(a, b))


# Time complexity: (m+n)*log(m+n)
# where m=len(a) and n=len(b)

# ---------------------------------------------------------------------------

# Solution 2: Efficient approach

def merge(a, b):
    res = []
    m = len(a)
    n = len(b)
    i = j = 0

    while i < m and j < n:
        if a[i] < b[j]:
            res.append(a[i])
            i = i + 1
        else:
            res.append(b[j])
            j = j + 1

    while i < m:
        res.append(a[i])
        i = i + 1

    while j < n:
        res.append(b[j])
        j = j + 1

    return res


a = [10, 15]
b = [5, 6, 6, 30, 40]

print(*merge(a, b))
