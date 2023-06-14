# Find the position of an element in a sorted array of Infinite numbers

def ans(arr, target):
    # first find the range
    # first start with box of size 2
    start = 0
    end = 1

    # condition for the target to lie in the range
    while target > arr[end]:
        # new start
        new_start = end + 1
        # double the box size New_end = previous_end + size_of_box * 2
        end = end + (end - start + 1) * 2
        start = new_start

    return infinite_array(arr, target, start, end)


def infinite_array(arr, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2

        # if target is greater than mid
        if target > arr[mid]:
            start = mid + 1

        # if target is less than mid
        elif target < arr[mid]:
            end = mid - 1

        # if target is equal to mid
        else:
            return mid

    # if element not found
    return -1


def main():
    arr = [2, 3, 5, 7, 10, 12, 13, 16, 18, 20, 21, 24, 27, 30]
    target = 18
    res = ans(arr, target)
    if res != -1:
        print(f"The position of {target} is present at index:", res)
    else:
        print(f"Target element {target} is not present in the given array:", res)


if __name__ == "__main__":
    main()

# Time complexity: O(log n)
# Space complexity: O(1)

