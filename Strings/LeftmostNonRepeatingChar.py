# Given a string, find it's first the index Leftmost  non-repeating character

# i/p : s="geeksforgeeks"      o/p : 5 (bcz "f" doesn't repeats)
# i/p : s="abcabc"             o/p : -1 (bcz no repeating char)
# i/p : s="apple"              o/p : 1 (bcz "a" doesn't repeats)


# 1. Naive approach

def leftmostNonRepeating1(s1):
    for i in range(len(s1)):
        flag = False
        for j in range(i + 1, len(s1)):
            if s1[i] == s1[j]:  # if char repeats then make flag=True
                flag = True
                break

        if flag == False:
            return i

    return -1


s1 = "geeksforgeeks"
print(leftmostNonRepeating1(s1))


# Time complexity: O(N^2)
# Space complexity: O(1)

# *****************************************************************************


# 2. Better approach

CHAR = 256


def leftmostNonRepeating2(s2):
    count = [0] * CHAR
    for i in range(len(s2)):
        count[ord(s2[i])] = count[ord(s2[i])] + 1

    for i in range(len(s2)):
        if count[ord(s2[i])] == 1:
            return i

    return -1


s2 = "abbcda"
print(leftmostNonRepeating2(s2))

# Time complexity: O(N)
# Space complexity: O(char)

# ****************************************************************************

# 3. Efficient approach

import sys

CHAR = 256


def leftmostNonRepeating3(s3):
    idx = [-1] * CHAR
    res = sys.maxsize

    for i in range(len(s3)):
        if idx[ord(s3[i])] == -1:  # first time traversing
            idx[ord(s3[i])] = i  # update -1 to index
        else:  # if repeated
            idx[ord(s3[i])] = -2

    for i in range(CHAR):
        if idx[i] >= 0:
            res = min(res, idx[i])

    if res == sys.maxsize:
        return -1
    else:
        return res


s3 = "aBbkdbaccd"
print(leftmostNonRepeating3(s3))

# Time complexity: O(N)
# Space complexity: O(1)
