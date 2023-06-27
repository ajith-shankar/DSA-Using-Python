# A panagram contains all the letters of english alphabet at least once.


def isPanagram(s):
    # your code here
    count = [False] * 26
    for i in s.lower():
        if i != " ":
            count[ord(i) - ord('a')] = True

    for j in count:
        if j == False:
            return False
    return True


s = "Thequickbrownfoxjumpsoverthelazydog"
print(isPanagram(s))


# Time complexity: O(N)
# Space complexity: O(1)
