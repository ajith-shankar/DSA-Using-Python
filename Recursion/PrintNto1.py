# Given a number N, the task is to print the numbers from N to 1.

# Input: N = 7
# Output: 7 6 5 4 3 2 1

def printNto1(n):
    if n <= 0:
        return
    print(n, end=" ")
    printNto1(n-1)


def main():
    n = 7
    printNto1(n)


if __name__ == "__main__":
    main()


# Time Complexity: O(N)
# Auxiliary Space: O(N)
