# Given a number N check if it is a palindrome.

# Solution 1:

def check_palindrome(n):
    if n < 0:
        return False
    else:
        temp = n
        reverse = 0
        while n != 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n = n // 10
        if reverse == temp:
            return True
        else:
            False


def main():
    n = -121
    print(f"Solution 1: Is {n} palindrome", check_palindrome(n))


if __name__ == "__main__":
    main()


# Time Complexity: O(log n)
# Space Complexity: O(1)

# *********************************************************************************************

# Solution 2:

def isPalindrome(n):
    if n < 0:
        return False
    res = 0
    temp = n
    while temp:
        temp, n = divmod(temp, 10)  # divmod() returns quotient and remainder
        res = (res * 10) + n
        return res == n


def main():
    n = 121
    print(f"Solution 2: Is {n} palindrome", isPalindrome(n))


if __name__ == "__main__":
    main()


# Time Complexity: O(1)
# Space Complexity: O(1)

# *************************************************************************************************

# Solution 3:

def check_palindrome(n):
    return str(n) == str(n)[:: -1]


def main():
    n = 10
    print(f"Solution 3: Is {n} palindrome", check_palindrome(n))


if __name__ == "__main__":
    main()

