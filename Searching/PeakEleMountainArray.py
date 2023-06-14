# Peak index in a mountain array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# https://leetcode.com/problems/find-peak-element/
# sorted array hence Binary search

def mountain_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2

        # decreasing part of the array
        if arr[mid] > arr[mid + 1]:
            end = mid  # this maybe the ans therefore end != mid-1

        else:  # arr[mid] < arr[mid + 1]
            start = mid + 1  # bcz mid+1 > mid element

    # start == end pointing to the largest element
    return start  # return end
    # bcz start & end always trying to find the largest element

