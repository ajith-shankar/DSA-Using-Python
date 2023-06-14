# Find the greatest number that is smaller than or equal to the target element

# sorted array use Binary search

def floor_of_num(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        # if target is equal to mid
        if target == arr[mid]:
            return mid

        # if target is less than mid
        elif target < arr[mid]:
            end = mid - 1

        # if target is greater than mid
        else:
            start = mid + 1

    # if element not found
    return end  # bcz while loop breaks when start becomes greater than end
    # so return smallest number (question says greatest num smaller than ~~or equal~~ to target num)


def main():
    arr = [2, 3, 5, 9, 14, 16, 18]
    target = 15
    res = floor_of_num(arr, target)
    if res != -1:
        print(f"The floor of the {target} is present at index:", res)
    else:
        print(f"Target element {target} is not present in the given array:", res)


if __name__ == "__main__":
    main()

# Time complexity: O(log n)
# Space complexity: O(1)

