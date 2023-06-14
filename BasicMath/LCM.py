# Find LCM of given two numbers

# LCM (Least Common Multiple) of two numbers is the smallest number which can be divided by both numbers.

# Solution 1: Naive approach

def find_lcm(a, b):
    res = max(a, b)

    while True:
        if res % a == 0 and res % b == 0:
            return res
        res = res + 1
    return res


def main():
    a = 3
    b = 7
    print(f"Solution 1: The LCM of {a} and {b} is", find_lcm(a, b))


if __name__ == "__main__":
    main()


# Time Complexity: theta(a*b - max(a,b))

# *********************************************************************************************

# Solution 2: Efficient way
# formula:  a * b = gcd(a, b) * lcm(a, b)
# rearrange the formula:  lcm(a, b) = (a * b)/gcd(a, b)

def find_gcd(a, b):
    if b == 0:
        return a
    return find_gcd(b, a % b)


def find_lcm(a, b):
    return (a * b) // find_gcd(a, b)


def main():
    a = 4
    b = 6
    print(f"Solution 2: The LCM of {a} and {b} is", find_lcm(a, b))


if __name__ == "__main__":
    main()

# Time Complexity: O(log(min(a,b))
# Auxiliary Space: O(log(min(a,b))



