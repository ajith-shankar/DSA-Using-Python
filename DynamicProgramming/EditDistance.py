# Given two strings str1 and str2 and below operations that can be performed on str1.
# Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.
#
# Insert
# Remove
# Replace
# All of the above operations are of equal cost.

# Input:   str1 = “geek”, str2 = “gesek”
# Output:  1
# Explanation: We can convert str1 into str2 by inserting a ‘s’.
#
# Input:   str1 = “cat”, str2 = “cut”
# Output:  1
# Explanation: We can convert str1 into str2 by replacing ‘a’ with ‘u’.
#
# Input:   str1 = “sunday”, str2 = “saturday”
# Output:  3
# Explanation: Last three and first characters are same.  We basically need to convert “un” to “atur”.  This can be done using below three operations. Replace ‘n’ with ‘r’, insert t, and insert a.


# 1. Using Recursion

def editDistance1(s1, s2, m, n):
    if m == 0:
        return n

    if n == 0:
        return m

    if s1[m-1] == s2[n-1]:  # if last chars are equal then
        return editDistance1(s1, s2, m-1, n-1)  # just move forward with the next chars

    else:
        return 1 + min(editDistance1(s1, s2, m, n-1), editDistance1(s1, s2, m-1, n), editDistance1(s1,s2, m-1, n-1))


if __name__ == "__main__":
    s1 = "SUNDAY"
    s2 = "SATURDAY"
    print(editDistance1(s1, s2, len(s1), len(s2)))


# Time complexity: O(3^m)  exponential

# ***************************************************************************************


# 2. Using DP (tabulation)

def editDistance2(s1, s2, m, n):
    dp = [[0]*(n+1) for i in range(m+1)]   # 2d array = [[0]*cols]*rows

    for i in range(m+1):  # base case
        dp[i][0] = i

    for j in range(n+1):  # base case
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    return dp[m][n]


if __name__ == "__main__":
    s1 = "CAT"
    s2 = "CUT"
    print(editDistance2(s1, s2, len(s1), len(s2)))


# Time complexity: O(m*n) ----> O(N)

