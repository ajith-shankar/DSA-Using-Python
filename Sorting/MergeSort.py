# divide and conquer
# it is Stable and Inplace algorithm (No extra space is required)

# Time complexity: O(N logN) ( for all best, average and worst)


def merge(a, low, mid, high):
    left = a[low: mid+1]  # left subarray
    right = a[mid+1: high+1]  # right subarray

    i = j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            k = k + 1
            i = i + 1
        else:
            a[k] = right[j]
            k = k + 1
            j = j + 1

    while i < len(left):
        a[k] = left[i]
        k = k + 1
        i = i + 1

    while j < len(right):
        a[k] = right[j]
        k = k + 1
        j = j + 1


def merge_sort(arr, low, high):
    if high > low:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)  # to sort the first half
        merge_sort(arr, mid+1, high)  # to sort the second half
        merge(arr, low, mid, high)  # to merge

    return arr


def main():
    arr = [10, 5, 30, 24, 7, 10]
    print("Merge sort: sorted array", merge_sort(arr, 0, 5))


if __name__ == "__main__":
    main()


# Time complexity: O(N logN)
# Space complexity: O(N)
