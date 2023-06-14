# Given a number, we need to find sum of its digits using recursion.

def sum_of_digit(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digit(n // 10)


def main():
    n = 2953
    res = sum_of_digit(n)
    print(res)


if __name__ == "__main__":
    main()


# Time Complexity: O(N)
# Auxiliary Space: O(N)
