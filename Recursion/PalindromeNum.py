# Given an integer, write a recursive function that checks if
# the given integer is a palindrome, else, not a palindrome.


def isPalin(num):
    n = str(num)
    size = len(n)

    if size == 0:
        return True
    return isPalRec(n, 0, size - 1)


def isPalRec(n, s, e):
    if s == e:
        return True

    if n[s] != n[e]:
        return False

    if s < e + 1:
        return isPalRec(n, s + 1, e - 1)
    return True


def main():
    num = 100
    if isPalin(num):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

# Time complexity: O(n)
# Space complexity: O(n)
