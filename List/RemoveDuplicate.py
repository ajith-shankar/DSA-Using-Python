# Given a sorted array, the task is to remove the duplicate elements from the array.

# Solution 1: Naive approach

def remove_duplicate(arr, n):
    # if array is empty or contains only one element
    if n == 0 or n == 1:
        return n

    # create an array of size n
    temp = list(range(n))

    # traversing
    j = 0
    for i in range(0, n - 1):
        if arr[i] != arr[i + 1]:
            temp[j] = arr[i]
            j = j + 1

    # Modify original array
    for i in range(0, j):
        arr[i] = temp[i]

    return j


def main():
    arr = [10, 20, 20, 30, 40, 40, 40, 50, 50]
    # arr = []
    n = len(arr)
    print(f"Solution 1: Array after removed duplicates and its size is:", remove_duplicate(arr, n))


if __name__ == "__main__":
    main()


# Time complexity: O(n)
# Space complexity: O(n)

# *********************************************************************************************

# Solution 2: Naive approach

def remove_dup(arr, n):
    # if array is empty or contains only one element
    if n == 0 or n == 1:
        return n

    # to store index of the next unique element
    j = 0

    # traversing
    for i in range(0, n - 1):
        if arr[i] != arr[i + 1]:
            arr[j] = arr[i]
            j = j + 1

    arr[j] = arr[n - 1]
    j = j+1
    return j


def main():
    arr = [10, 20, 20, 30, 40, 40, 40, 50, 50]
    # arr = []
    n = len(arr)
    print(f"Solution 2: Array after removed duplicates and its size is:", remove_duplicate(arr, n))


if __name__ == "__main__":
    main()


# Time complexity: O(n)
# Space complexity: O(1)
