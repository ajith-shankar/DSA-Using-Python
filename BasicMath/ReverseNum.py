# Given a number N reverse the number and print it.

# Solution 1: Using While loop

def reverse_num(n):
    reverse = 0
    while n != 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    return reverse


def main():
    n = 1947
    print(f"Solution 1: Reverse of a {n} is", reverse_num(n))


if __name__ == "__main__":
    main()


# Time complexity O(log10 n)
# Space complexity O(1)

# *************************************************************************************

# Solution 2: Using String slicing

def reverse_num(n):
    x = str(n)
    return int(x[:: -1])


def main():
    n = 1234
    print(f"Solution 2: Reverse of a {n} is", reverse_num(n))


if __name__ == "__main__":
    main()

# Time complexity O(n)
# Space complexity O(1)

# **********************************************************************************************
