# Check if a String is Subsequence of Other
# subsequence: you can remove any character but remaining characters should be in order
# Ex: S1="ABC"  subsequence: "", A, B, C, AB, AC, BC, ABC (it is always 2^N where N=len(s1))
# but BA, CA, CAB, BAC are not the subsequence

# 1. Naive approach

def isSubSeq(s1, s2):
    i = 0
    j = 0
    if len(s1) < len(s2):
        return False
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            j = j + 1

        i = i + 1

    if j == len(s2):
        return True
    else:
        return False


s1 = "ABCDEF"
s2 = "ADE"
print(isSubSeq(s1, s2))


# Time complexity: O(m) where m=len(s1)
# Space complexity: O(1)

# *************************************************************************

# 2. Using Recursion

def isSubSeq2(str1, str2, m, n):
    # if len(s2) becomes 0
    if n == 0:
        return True
    if m == 0:
        return False
    if str1[m - 1] == str2[n - 1]:
        return isSubSeq2(str1, str2, m - 1, n - 1)
    else:
        return isSubSeq2(str1, str2, m - 1, n)


st1 = "gksrek"
st2 = "geeksforgeeks"
k = len(st1)
l = len(st2)
print(isSubSeq2(st1, st2, k, l))

# Time complexity: O(m+n)
# Space complexity: O(N)

# *****************************************************************************


# 3. Using DP

dp = [[-1] * 50] * 50  # 2Darr = [[0]*cols]*rows


def isSubSeq3(ip_str1, ip_str2, x, y):
    if x == 0 or y == 0:
        return 0

    if dp[x][y] != -1:
        return dp[x][y]

    if ip_str1[x - 1] == ip_str2[y - 1]:
        dp[x][y] = 1 + isSubSeq3(ip_str1, ip_str2, x - 1, y - 1)
        return dp[x][y]

    else:
        dp[x][y] = isSubSeq3(ip_str1, ip_str2, x, y - 1)
        return dp[x][y]


ip_str1 = "gksgek"
ip_str2 = "geeksforgeeks"
x = len(ip_str1)
y = len(ip_str2)

if isSubSeq3(ip_str1, ip_str2, x, y) == x:
    print("True")
else:
    print("False")