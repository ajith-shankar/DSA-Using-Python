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
        res =
