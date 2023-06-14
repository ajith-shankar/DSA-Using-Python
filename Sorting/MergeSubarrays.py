# We are given an array with two subarrays, we need to merge these subarrays and make sorted array.

# input: a = [10, 15, 20, 11, 13], low = 0, high = 4 and mid = 2 , here low <= mid < high
# output: a = [10, 11, 13, 15, 20]

def merge_sub(arr, low, mid, high):
    # left sub array
    left = arr[low:mid + 1]
    # right sub array
    right = arr[mid + 1:high + 1]
    i = j = 0
    k = low  # bcz low can be anywhere

    # now use merge two sorted array technique
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            k = k + 1
            i = i + 1
        else:
            arr[k] = right[j]
            k = k + 1
            j = j + 1

    while i < len(left):
        arr[k] = left[i]
        k = k + 1
        i = i + 1

    while j < len(right):
        arr[k] = right[j]
        k = k + 1
        j = j + 1

    return arr


arr = [10, 15, 20, 11, 13]
print(merge_sub(arr, 0, 2, 4))


# Time complexity: O(m+n)
# Space complexity: O(m+n)
# where m=len(left) and n=len(right)
