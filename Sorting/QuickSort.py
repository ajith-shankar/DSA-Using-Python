# Divide and Conquer
# In place algorithm
# It is not stable

# Time complexity: O(N^2) (worst case)
# even-though O(N^2) in worst case, it is still considered Faster than merge sort


# Quick sort using Lomuto partition

def quick_sort(lst, low, high):
    if low < high:
        p = lomuto_partition(lst, low, high)
        quick_sort(lst, low, p - 1)
        quick_sort(lst, p + 1, high)


def lomuto_partition(lst, low, high):
    pivot = lst[high]
    i = low - 1

    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1


lst = [8, 4, 7, 9, 3, 10, 5]
quick_sort(lst, 0, 6)
print(lst)

# Time complexity: O(N)
# space complexity: O(1)

# ---------------------------------------------------------------------------------

# Quick sort using Hoare partition

def quick_sort2(lst1, l, h):
    if l < h:
        p = hoare_partition(lst1, l, h)
        quick_sort2(lst1, l, p)
        quick_sort2(lst1, p+1, h)


def hoare_partition(lst1, l, h):
    pivot = lst1[l]
    i = l - 1
    j = h + 1

    while True:
        i += 1
        while lst1[i] < pivot:
            i += 1

        j -= 1
        while lst1[j] > pivot:
            j -= 1

        if i >= j:
            return j

        lst1[i], lst1[j] = lst1[j], lst1[i]


lst1 = [8, 4, 7, 9, 3, 10, 5]
quick_sort2(lst1, 0, 6)
print(lst1)

# Time complexity: O(N)
# space complexity: O(1)

