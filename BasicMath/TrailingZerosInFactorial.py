# Given an integer n, write a function that returns count of trailing zeroes in n!.

# Input: n = 5
# Output: 1
# Factorial of 5 is 120 which has one trailing 0.
#
# Input: n = 20
# Output: 4
# Factorial of 20 is 2432902008176640000 which has
# 4 trailing zeroes.
#
# Input: n = 100
# Output: 24

# Trailing 0s in n! = Count of 5s in prime factors of n!
#                   = floor(n/5) + floor(n/25) + floor(n/125) + ....


def trailing_zeros(n):
    count = 0
    i = 5
    # keep dividing n by powers of 5 and update the count
    while n // i >= 1:
        count = count + n // i
        i = i * 5
    return count


n = 100
print(f"Solution 1: Trailing zeros in factorial of {n} is", trailing_zeros(n))


# Time complexity O(log5 n)
# Space complexity O(1)
