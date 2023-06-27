def reverse(in_str):
    rev = ""
    for i in in_str:
        rev = i + rev
    return rev


if __name__ == "__main__":
    s = "Geek"
    print(reverse(s))


# Time complexity: O(N)
# Space complexity: O(1)
