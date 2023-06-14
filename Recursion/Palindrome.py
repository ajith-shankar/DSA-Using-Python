# Given a string, write a recursive function that checks if
# the given string is a palindrome, else, not a palindrome.

def is_palindrome(ip_text):
    n = len(ip_text)

    # if string is empty
    if n == 0:
        return True

    return is_pal_rec(ip_text, 0, n-1)


def is_pal_rec(ip_text, s, e):
    # if there is only one character
    if s == e:
        return True

    # if first and last char do not match
    if ip_text[s] != ip_text[e]:
        return False

    # if there are more than two characters, check if middle substring is also palindrome or not
    if s < e+1:
        return is_pal_rec(ip_text, s+1, e-1)

    return True


def main():
    ip_text = "malayalam"
    if is_palindrome(ip_text):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()


# Time complexity: O(n)
# Space complexity: O(n)
