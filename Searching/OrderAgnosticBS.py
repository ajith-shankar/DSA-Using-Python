# Given a sorted array, but we don't know it is Ascending or Descending order

def order_agnostic_BS(arr, target):
    start = 0
    end = len(arr) - 1

    # find the order
    isAsc = arr[start] < arr[end]

    while start <= end:
        # find middle element
        mid = start + (end - start) // 2

        # if target is present at the middle
        if target == arr[mid]:
            return mid

        # for ascending order
        if isAsc:
            # if target element is lesser than mid
            if target < arr[mid]:
                end = mid - 1

            # if target element is greater than mid
            else:
                start = mid + 1

        # for descending order
        else:
            # if target element is greater than mid
            if target > arr[mid]:
                end = mid - 1

            # if target element is lesser than mid
            else:
                start = mid + 1

    # if target element is not present in the array
    return -1


def main():
    arr = [100, 80, 60, 40, 20, 10]
    target = 20
    res = order_agnostic_BS(arr, target)
    if res != -1:
        print(f"Target element {target} is present at index:", res)
    else:
        print(f"Target element {target} is not present in the given array:", res)


if __name__ == "__main__":
    main()

# Time complexity: O(log n)
# Space complexity: O(1)
