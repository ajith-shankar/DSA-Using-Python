# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Search in Rotated sorted array (ascending order)

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Approach
# 1. Find the pivot, pivot: from where your next numbers are in ascending order or largest number in the array
# 2. Find in first half otherwise second half

def search(nums, target):
    pivot = find_pivot(nums)
    # if you not found pivot, i.e. array is not rotated
    if pivot == -1:
        return binary_search(nums, target, 0, len(nums) - 1)

    # if you found pivot
    elif nums[pivot] == target:
        return pivot

    elif target >= nums[0]:
        return binary_search(nums, target, 0, pivot - 1)

    return binary_search(nums, target, pivot + 1, len(nums) - 1)


def binary_search(arr, target, start, end):
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


def find_pivot(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        # [4,5,6,7,0,1,2] here 7 is the pivot
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid
        elif mid > start and arr[mid] < arr[mid - 1]:
            return mid - 1
        elif arr[mid] <= arr[start]:
            end = mid - 1
        else:
            start = mid + 1
    # if not found
    return -1


def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    search(nums, target)
    print("Index of the target element is:", search(nums, target))


if __name__ == "__main__":
    main()

