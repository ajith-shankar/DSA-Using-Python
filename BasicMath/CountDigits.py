# Given an integer N , write program to count number of digits in N.

# Solution 1:

def count_digits(n):
    count = 0
    while n != 0:
        n = n // 10  # floor division
        count = count + 1
    return count


def main():
    n = 2023
    print(f"Solution 1: No of digits in {n} is", count_digits(n))


if __name__ == "__main__":
    main()


# time complexity O(n)
# space complexity O(1)

# *******************************************************************************

# Solution 2: Convert the integers to string and find the length

def count_digits(n):
    x = str(n)
    return len(x)


def main():
    n = 70401
    print(f"Solution 2: No of digits in {n} is", count_digits(n))


if __name__ == "__main__":
    main()

# Time complexity O(1)
# Space complexity O(1)

# **************************************************************************************

# Solution 3: using logarithm base 10

import math


def count_digits(n):
    digi = math.floor(math.log10(n) + 1)
    return digi


def main():
    n = 1234567
    print(f"Solution 3: No of digits in {n} is", count_digits(n))


if __name__ == "__main__":
    main()

# Time complexity O(1)
# Space complexity O(1)
