# Given two numbers. The task is to find the GCD of the two numbers
# The GCD of two integers X and Y is the largest number that divides both of X and Y
# (without leaving a remainder).

# Solution 1: using math module math.gcd() function compute the greatest common divisor of 2 numbers mentioned in its arguments.

import math

a = 60
b = 48
print(f"Solution 1: GCD of {a} and {b} is", math.gcd(a, b))


# *********************************************************************************************

# Solution 2: Euclidean Algorithm

def find_gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a  # we can return a or b


def main():
    a = 60
    b = 48
    print(f"Solution 2: GCD of {a} and {b} is", find_gcd(a, b))


if __name__ == "__main__":
    main()

# Time complexity: O(


# *********************************************************************************************

# Solution 3: Optimized  Euclidean Algorithm (with recursion)

def find_gcd(a, b):
    if b == 0:
        return a
    return find_gcd(b, a % b)


def main():
    a = 12
    b = 15
    print(f"Solution 3: GCD of {a} and {b} is", find_gcd(a, b))


if __name__ == "__main__":
    main()


# ********************************************************************************************

# Solution 4: With recursion

def find_gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    if a == b:
        return a

    # if a is greater
    if a > b:
        return find_gcd(a-b, b)
    return find_gcd(a, b-a)


def main():
    a = 12
    b = 15
    if find_gcd(a, b):
        print(f"Solution 4: GCD of {a} and {b} is", find_gcd(a, b))
    else:
        print("Not found")

    if __name__ == "__main__":
        main()
