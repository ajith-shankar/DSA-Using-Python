# It is also known as Sinking sort/Exchange sort
# it is Stable and Inplace algorithm (No extra space is required)

# Time complexity:
# Best-case: O(n) if array is sorted
# Worst-case: O(n^2) if array is not sorted

def bubble_sort(arr):
    n = len(arr)

    # run the steps n-1 times
    for i in range(n - 1):
        swapped = False
        # for each step, max element come at the last respective index
        for j in range(n - i - 1):
            # swap if item is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # if you didn't swap for a particular value of i that means array is sorted
        # if swapped == False, then stop the loop
        if not swapped:
            return arr


def main():
    arr = [5, 3, 4, 1, 2]
    print("Bubble sort, Sorted array:", bubble_sort(arr))


if __name__ == "__main__":
    main()


# Time complexity: O(n^2)
# Space complexity: O(1)
