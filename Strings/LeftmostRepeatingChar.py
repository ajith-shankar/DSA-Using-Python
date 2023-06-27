# Given a string we need to find out leftmost character that repeats

# i/p : s1="geeksforgeeks"    o/p : 0 (bcz "g" occurred 2 times)
# i/p : s1="abbccbc"          o/p : 1 (bcz "b" occurred 3 times)


# 1. Naive approach

def leftmost_repeating1(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                return i  # return leftmost index
    return -1


s = "cabbad"
print(leftmost_repeating1(s))


# Time complexity: O(N^2)
# Space complexity: O(1)

# *****************************************************************************


# 2. Better approach

def leftmost_repeating2(s1):
    char = 256
    # count array
    count = [0] * char
    for i in range(len(s1)):
        count[ord(s1[i])] = count[ord(s1[i])] + 1  # count[65] = count[65] + 1 ----> 0+1 = 1
    for i in range(len(s1)):
        if count[ord(s1[i])] > 1:
            return i
    return -1


s1 = "ccabbad"
print(leftmost_repeating2(s1))

# Time complexity: O(N) but 2 traversal required
# Space complexity: O(1)

# **********************************************************************************


# 3. Efficient approach

import sys


def leftmost_repeating3(s2):
    char = 256
    # creating index array
    idx = [-1] * char
    res = sys.maxsize  # infinite
    for i in range(len(s2)):
        if idx[ord(s2[i])] == -1:
            idx[ord(s2[i])] = i
        else:
            res = min(res, idx[ord(s2[i])])

    if res == sys.maxsize:
        return -1
    else:
        return res


s2 = "cabbdcac"
print(leftmost_repeating3(s2))


# Time complexity: O(N) but 1 traversal required
# Space complexity: O(1)

# *************************************************************************************


# 4. Efficient approach 2

def leftmost_repeating4(s3):
    char = 256
    # creating visited array
    visited = [False] * char
    res = -1
    for i in range(len(s3) - 1, -1, -1):  # traversing in reverse order
        if visited[ord(s3[i])] == True:
            res = i
        else:
            visited[ord(s3[i])] = True
    return res


s3 = "abccbd"
print(leftmost_repeating4(s3))


# Time complexity: O(N)
# Space complexity: O(1)
