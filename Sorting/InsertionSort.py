# used in practice if array is small
# it is Stable and Inplace algorithm (No extra space is required)

# Time complexity:
# Best-case: O(n) if array is sorted
# Worst-case: O(n^2) if array is in reverse order


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j = j - 1

    return arr


def main():
    arr = [5, 3, 4, 1, 2]
    print("Insertion sort, Sorted array:", insertion_sort(arr))


if __name__ == "__main__":
    main()

# Time complexity: O(n^2)
# Space complexity: O(1)
