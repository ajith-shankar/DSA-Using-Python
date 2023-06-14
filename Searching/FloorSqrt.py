# Given an integer X, find its square root. If X is not a perfect square, then return floor(√x).
#
# Examples :
#
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2.
#
# Input: x = 11
# Output: 3
# Explanation:  The square root of 11 lies in between 3 and 4 so floor of the square root is 3.

def floor_sqrt(x):
    # base case
    if x == 0 or x == 1:
        return x

    # binary search to find the sqrt
    start = 1
    end = x // 2
    while start <= end:
        mid = (start + end) // 2

        # if x is a perfect square
        if mid * mid == x:
            return mid

        # if x is not a perfect square, then
        # (mid * mid) is lesser than the x
        if (mid * mid) < x:
            start = mid + 1
            ans = mid

        # if (mid * mid) is greater than x
        else:
            end = mid - 1

    return ans


def main():
    x = 11
    print(f"Floor square of {x} is:", floor_sqrt(x))


if __name__ == "__main__":
    main()

# Time complexity: O(log x)
# Space complexity: O(1)
