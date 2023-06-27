# Given an array of N non-negative integers arr[] representing an elevation map where
# the width of each bar is 1, compute how much water it is able to trap after raining.

# Input: arr[]   = {3, 0, 2, 0, 4}
# Output: 7
# Explanation: Structure is like below.
# We can trap “3 units” of water between 3 and 2,
# “1 unit” on top of bar 2 and “3 units” between 2 and 4.

# Solution 1: Brute Force approach

def max_water(arr, n):
    res = 0

    # for every element in the array
    for i in range(1, n - 1):
        # find the max element on its left
        left = arr[i]
        for j in range(0, i):
            left = max(left, arr[j])

        # find the max element on its right
        right = arr[i]
        for j in range(i + 1, n):
            right = max(right, arr[j])

        # update the max water
        res = res + min(left, right) - arr[i]

    return res


def main():
    arr = [3, 0, 2, 0, 4]
    n = len(arr)
    print("Solution 1:Maximum water can store is:", max_water(arr, n))


if __name__ == "__main__":
    main()


# Time complexity: O(n^2)
# Space complexity: O(1)

# **************************************************************************************

# Solution 2: Efficient solution based on PreCalculation concept

def rain_water(arr, n):
    # create an array to store left max
    left = [0] * n
    # create an array to store  right max
    right = [0] * n

    res = 0

    # now fill left array
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])

    # now fill right array
    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):  # reverse order
        right[i] = max(right[i + 1], arr[i])

    # Calculate the accumulated water element by element
    for i in range(0, n):
        res = res + min(left[i], right[i]) - arr[i]

    return res


def main():
    arr = [3, 0, 2, 0, 4]
    n = len(arr)
    print("Solution 2:Maximum water can store is:", rain_water(arr, n))


if __name__ == "__main__":
    main()


# Time complexity: O(n)
# Space complexity: O(n)

# ***************************************************************************************

# https://leetcode.com/problems/trapping-rain-water/

def trap(height):
    l = 0
    r = len(height) - 1
    res = 0
    leftMax = height[l]
    rightMax = height[r]
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]

    return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))

# Time complexity: O(n)
# Space complexity: O(1)

