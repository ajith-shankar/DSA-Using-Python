# Given an array arr[] of N integers, the task is to find the maximum difference between any two elements of the array.
# where arr[j]-arr[i] such that j>i

# 1. Naive approach

def max_diff1(arr):
    n = len(arr)
    res = arr[1] - arr[0]
    for i in range(0, n-1):
        for j in range(i+1, n):
            res = max(res, arr[j]-arr[i])

    return res


arr = [2, 3, 10, 6, 4, 8, 1]
print(max_diff1(arr))

# Time complexity: O(N^2)
# Space complexity: O(1)

# *****************************************************************************************


# 2. Efficient approach

def max_diff2(arr):
    n = len(arr)
    res = arr[1]-arr[0]
    min_val = arr[0]
    for j in range(1, n):
        res = max(res, arr[j]-min_val)
        min_val = min(arr[j], min_val)
    return res


arr = [2, 3, 10, 6, 4, 8, 1]
print(max_diff2(arr))

# Time complexity: O(N)
# Space complexity: O(1)

# *****************************************************************************************

