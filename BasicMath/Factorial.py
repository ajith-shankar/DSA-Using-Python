# Write a program to compute Factorial of N
#  Factorial of 4 means 4*3*2*1 = 24

# Solution 1:

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n > 0:
            fact = fact * n
            n = n - 1
        return fact


def main():
    n = 3
    print(f"Solution 1: Factorial of {n} is", factorial(n))


if __name__ == "__main__":
    main()


# Time complexity O(n)
# Space complexity O(1)

# **********************************************************************************************

# Solution 2: Using Recursion

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    n = 5
    print(f"Solution 2: Factorial of {n} is", factorial(n))


if __name__ == "__main__":
    main()

# Time complexity O(n)
# Space complexity O(1)
