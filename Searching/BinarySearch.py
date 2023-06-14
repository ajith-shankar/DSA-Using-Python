# Binary search works only for Sorted array

# iterative implementation of binary search

def binary_search(arr, target):
    start = 0
    end = len(arr)-1

    while start <= end:
        # find middle element
        mid = start + (end - start) // 2

        # if target element is lesser than mid
        if target < arr[mid]:
            end = mid - 1

        # if target element is greater than mid
        elif target > arr[mid]:
            start = mid + 1

        # if target element is present at mid
        else:
            return mid

    # if target element is not present in the array
    return -1


def main():
    arr = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]
    target = 80
    res = binary_search(arr, target)
    if res != -1:
        print(f"Target element {target} is present at index:", res)
    else:
        print(f"Target element {target} is not present in the given array:", res)


if __name__ == "__main__":
    main()


# Time complexity: O(log n)
# Space complexity: O(1)
