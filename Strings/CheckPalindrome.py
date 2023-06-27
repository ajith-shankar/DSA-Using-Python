# Given a string, write a python function to check if it is palindrome or not.

# i/p : s1="radar"          s1="abA"
# o/p : Yes                 No

def checkPalindrome(s):
    low = 0
    high = len(s) - 1
    while low < high:
        if s[low] != s[high]:
            print("No")
            break
        low += 1
        high -= 1
    else:
        print("Yes")


if __name__ == "__main__":
    str1 = "radar"
    checkPalindrome(str1)


# Using string slicing
def isPalindrome(ip_str):
    return ip_str == ip_str[::-1]


if __name__ == "__main__":
    s1 = "radix"
    ans = isPalindrome(s1)
    if ans:
        print("Yes")
    else:
        print("No")
