# Given a sorted array arr[] with possibly duplicate elements, the task is to find indexes of the first and last occurrences of an element x in the given array.

# Input : arr[] = {1, 3, 5, 5, 5, 5, 67, 123, 125}, x = 5
# Output : First Occurrence = 2
#         Last Occurrence = 5
#
# Input : arr[] = {1, 3, 5, 5, 5, 5, 7, 123, 125 }, x = 7
# Output : First Occurrence = 6
#         Last Occurrence = 6


def first_occur(arr, target, start, end, size):
    while start <= end:
        mid = start + (end - start) // 2

        if mid == 0 or arr[mid - 1] < target == arr[mid]:  # target > arr[mid-1] and arr[mid]==target
            return mid

        # if target element is greater than arr[mid]
        elif target > arr[mid]:
            return first_occur(arr, target, mid+1, end, size)

        # if target element is less than arr[mid]
        else:
            return first_occur(arr, target, start, mid-1, size)

    # if target element is not present
    return -1


def last_occur(arr, target, start, end, size):
    while start <= end:
        mid = start + (end - start) // 2

        if mid == size-1 or arr[mid + 1] > target == arr[mid]:  # target < arr[mid+1] and arr[mid]==target
            return mid

        # if target element is lesser than the arr[mid]
        elif target < arr[mid]:
            return last_occur(arr, target, start, mid-1, size)

        # if target element is greater than the arr[mid]
        else:
            return last_occur(arr, target, mid+1, end, size)

    return -1


def main():
    arr = [1, 3, 5, 5, 5, 5, 7, 123, 125]
    target = 5
    start = 0
    end = len(arr)-1
    size = len(arr)
    print(f"The first occurrence of the the {target} is", first_occur(arr, target, start, end, size))
    print(f"The first occurrence of the the {target} is", last_occur(arr, target, start, end, size))


if __name__ == "__main__":
    main()

# Time complexity: O(log n)
# Space complexity: O(1)
