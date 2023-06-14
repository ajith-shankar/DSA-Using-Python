# Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[]. Expected time complexity is O(Logn)

# Input: arr[] = {1, 1, 2, 2, 2, 2, 3}   x = 2
# Output: 4

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end-start) // 2

        if arr[mid] == target:
            return mid

        elif target > arr[mid]:
            start = mid + 1

        else:
            end = mid - 1

    return -1


def count_occurrence(arr, target):
    idx = binary_search(arr, target)

    # if element is not present
    if idx == -1:
        return 0

    # count occurrence
    # left side count
    count = 1
    left = idx - 1
    while left >= 0 and arr[left] == target:
        count += 1
        left -= 1

    # right side
    right = idx + 1
    while right < len(arr) and arr[right] == target:
        count += 1
        right += 1

    return count


def main():
    arr = [1, 1, 2, 2, 2, 2, 3]
    target = 5
    print(f"Count of {target} is:", count_occurrence(arr, target))


if __name__ == "__main__":
    main()

# Time complexity: O(log n)
# Space complexity: O(1)

