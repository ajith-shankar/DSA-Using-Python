# second largest element

def second_largest(arr):
    if len(arr) < 1:
        return None

    lar = arr[0]
    slar = None

    for x in arr[1:]:
        if x > lar:
            slar = lar
            lar = x
        elif x != lar:
            if slar == None or slar < x:
                slar = x

    return slar


arr = [12, 35, 1, 10, 34, 1]
print(second_largest(arr))


# Time complexity: O(N)
# Space complexity: O(1)

