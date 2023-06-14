# Does less memory writes
# It is not Stable and Inplace algorithm (No extra space is required)

# Time complexity:
# Best-case: O(n^2) if array is sorted
# Worst-case: O(n^2) if array is not sorted

# Space complexity: O(1)

def selection_sort(arr):
    n = len(arr)

    # if arr size is 6 we are running i loop for 6-2=4 times
    for i in range(n - 1):
        min_idx = i
        # find the smallest element and swap with correct index
        for j in range(i + 1, n):
            # find index of the smallest element
            if arr[j] < arr[min_idx]:
                min_idx = j
        # swap
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

    return arr


def main():
    arr = [5, 3, 2, 4, 1]
    print("Selection sort, Sorted array:", selection_sort(arr))


if __name__ == "__main__":
    main()
