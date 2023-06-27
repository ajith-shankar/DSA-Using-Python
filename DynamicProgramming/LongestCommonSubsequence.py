# Given two sequences, find the length of the longest subsequence present in both of them.
# A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

# i/p : s1="ADF"  subsequences are "", "A", "D", "F", "AD", "AF", "DF", "ADF"
# s2 = "ABD"  subsequences are "", "A", "B", "D", "AB", "AD", "BD", "ABD"

# o/p : 2. Because common subsequences between s1 and s2 are "A", "D", and "AD"
# so the longest common subsequence is "AD". Then length of "AD" is 2

# 1. solving using Recursion:

def lcsRec(s1, s2, m, n):
    if m == 0 or n == 0:  # if len() becomes 0
        return 0

    # we are traversing in reverse order
    if s1[m - 1] == s2[n - 1]:  # if last chars of s1 and s2 are equal then add 1 and check the next chars
        return 1 + lcsRec(s1, s2, m - 1, n - 1)

    else:
        return max(lcsRec(s1, s2, m - 1, n), lcsRec(s1, s2, m, n - 1))


s1 = "ADF"
s2 = "ABD"
print(lcsRec(s1, s2, len(s1), len(s2)))

# Time complexity: O(2^max(m, n)) -----> O(2^N)
# Space complexity: O(N)

# ******************************************************************************************

# 2. Using Memoization (Top Down)

# creating 2D array, arr = [[0]*cols]*rows
rows = 100
cols = 100
dp = [[-1 for i in range(cols)] for j in range(rows)]


def lcsMemo(s1, s2, m, n):
    # if chars already processed and dp array has value other than -1
    if dp[m][n] != -1:
        return dp[m][n]

    # base condition
    if m == 0 or n == 0:
        dp[m][n] = 0

    else:
        if s1[m - 1] == s2[n - 1]:  # traversing from last char
            dp[m][n] = 1 + lcsMemo(s1, s2, m - 1, n - 1)

        else:
            dp[m][n] = max(lcsMemo(s1, s2, m - 1, n), lcsMemo(s1, s2, m, n - 1))

    return dp[m][n]


s1 = "AGGTAB"
s2 = "GXTXAYB"
print(lcsMemo(s1, s2, len(s1), len(s2)))  # GTAB


# Time complexity: O(m*n) ----> O(N)
# Space complexity: O(N)

# **************************************************************************************

# 3. Tabulation (Bottom up)

def lcsTab(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[None] * (n+1) for i in range(m+1)]
    # print(dp)
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0

            elif s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # print(dp)
    return dp[m][n]


s1 = "ADF"
s2 = "AD"
print(lcsTab(s1, s2))

# Time complexity: O(m*n) ----> O(N)
# Space complexity: O(N)

