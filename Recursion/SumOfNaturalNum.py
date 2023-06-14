# Given a number n, find sum of first n natural numbers.

def sum_naturals(n):
    if n <= 1:
        return n
    return n + sum_naturals(n-1)


def main():
    n = 5
    res = sum_naturals(n)
    print(res)


if __name__ == "__main__":
    main()

# Time complexity: O(n)
# Space complexity: O(n)
