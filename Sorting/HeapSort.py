# It is a optimization over Selection sort
# Not stable and in place algo


# Time complexity: O(N logN)
# Space complexity: O(1)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        # swap
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


def heapify(arr, n, i):
    # initialize a largest as root
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def main():
    arr = [12, 11, 13, 5, 6, 7]
    heap_sort(arr)
    print("Sorted array: Heap sort:", arr)


if __name__ == "__main__":
    main()


# Time complexity: O(N logN)
# Space complexity: O(1)

