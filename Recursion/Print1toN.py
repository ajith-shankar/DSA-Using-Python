# Given a number N, the task is to print the numbers from 1 to N.

# Input: N = 7
# Output: 1 2 3 4 5 6 7

def print1toN(n):
    if n <= 0:
        return
    print1toN(n - 1)
    print(n, end=" ")


def main():
    n = 7
    print1toN(n)


if __name__ == "__main__":
    main()


# Time Complexity: O(N)
# Auxiliary Space: O(N)
