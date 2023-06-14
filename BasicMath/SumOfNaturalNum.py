# Write a program to compute sum of N natural numbers

# Solution 1: using mathematical formula (N*(N+!))/2

def SumOfNaturalNum(n):
    return n * (n + 1) // 2  # floor division return integer


def main():
    n = 10
    print(f"Solution 1: Sum of {n} number is", SumOfNaturalNum(n))


if __name__ == "__main__":
    main()


# Time complexity O(1)
# Space complexity O(1)
# The above program causes overflow

# ***********************************************************************************************

# Solution 2: using mathematical formula, to avoid overflow
# by dividing n we can avoid overflow some extent

def SumOfNaturalNum(n):
    # if n is even
    if n % 2 == 0:
        return (n // 2) * (n + 1)  # taking floor division
    # if n is odd
    else:
        return ((n + 1) // 2) * n


def main():
    n = 4
    print(f"Solution 2: Sum of {n} number is", SumOfNaturalNum(n))


if __name__ == "__main__":
    main()

# Time complexity O(n)
# Space complexity O(1)

# ************************************************************************************************

# Solution 3: Using iterative method

def SumOfNaturalNum(n):
    sum = 0
    while n > 0:
        sum = sum + n
        n = n - 1
    return sum


def main():
    n = 2
    print(f"Solution 3: Sum of {n} number is", SumOfNaturalNum(n))


if __name__ == "__main__":
    main()

# Time complexity O(n)
# Space complexity O(1)

# **************************************************************************************************
