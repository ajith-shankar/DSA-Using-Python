# write a program to count inversions in an array
# Inversion means,  a pair (arr[i], arr[j]) forms an inversion where i < j and arr[i] > arr[j]

# If array is sorted then inversion count is 0
# If array is decreasing order then inversion count is (n*(n-1))/2


# Solution 1: Naive approach

# def count_inversion_1(arr):
#     n = len(arr)
#     count = 0
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if arr[i] > arr[j]:
#                 count += 1
#     return count
#
#
# arr = [2, 4, 1, 3, 5]
# print(count_inversion_1(arr))


# (2, 1), (4, 1), (4, 3)    where i < j  and arr[i] > arr[j]

# Time complexity: O(n^2)
# Space complexity: O(1)

# ----------------------------------------------------------------------------------------------

# Solution 2: Efficient approach (using Merge sort)

def count_inversion_2(arr, low, high):
    count = 0
    if low < high:
        mid = (low + high) // 2
        count = count + count_inversion_2(arr, low, mid)  # first half
        count = count + count_inversion_2(arr, mid + 1, high)  # second half
        count = count + count_merge(arr, low, mid, high)

    return count


def count_merge(arr, low, mid, high):
    left = arr[low: mid + 1]
    right = arr[mid + 1: high + 1]
    res, i, j, k = 0, 0, 0, low
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
            res = res + (len(left) - 1)  # left is greater

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return res


def main():
    arr = [10, 5, 30, 15, 7]
    n = len(arr)
    print(count_inversion_2(arr, 0, n))


if __name__ == "__main__":
    main()

# wrong
# Time complexity: O(N logN)
# Space complexity: O(1)

