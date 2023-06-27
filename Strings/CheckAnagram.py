# Check whether two Strings are anagram of each other

# An anagram of a string is another string that contains the same characters, only the order of characters can be different.

# Ex: s1="abcd" and s2="dacb"
# s1="listen" and s2="silent"

# 1. Using Naive approach

def areAnagram1(s1, s2):
    if len(s1) != len(s2):
        return False

    s1 = sorted(s1)  # aaabc
    s2 = sorted(s2)  # aaabc
    if s1 == s2:
        return True


s1 = "abaac"
s2 = "acbaa"
print(areAnagram1(s1, s2))


# Time complexity: O(N logN)
# Space complexity: O(1)

# *******************************************************************


# 2. Efficient algorithm

def areAnagram2(str1, str2):
    # if lengths are not equal then it's not anagram
    if len(str1) != len(str2):
        return False

    # create count array of size 256 and initialize 0 for all the index
    count = [0] * 256  # ascii char len

    for i in range(len(str1)):
        count[ord(str1[i])] = count[ord(str1[i])] + 1  # ord() gives you ascii value of the character
        count[ord(str2[i])] = count[ord(str2[i])] - 1  # 0 ---> 1 for s1 and 0 ---> -1 for s2, so 1-1=0

    for x in count:
        if x != 0:
            return False
    return True


str1 = "listen"
str2 = "silent"
print(areAnagram2(str1, str2))


# Time complexity: O(N)
