# Given an array of integers and a number k, find the maximum sum of a subarray of size k.

# Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
#          k = 4
# Output : 39
# We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.

# Solution 1: Naive approach

def MaxSum(arr, n, k):
    # If k is lesser than n
    if k < n:
        print("Invalid")
        return -1

    # compute sum of first window of size k
    res = arr[0]
    for i in range(0, k):
        pass


# ************************************************************************

# https://leetcode.com/problems/maximum-subarray/

def max_sub_sum(arr):
    maxSub = arr[0]
    currSub = 0

    for i in arr:
        if currSub < 0:  # if we encounter -ve values then make currSub as 0
            currSub = 0

        currSub = currSub + i
        maxSub = max(maxSub, currSub)
    return maxSub


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub_sum(arr))

# Time complexity: O(n)
# Space complexity: O(1)
