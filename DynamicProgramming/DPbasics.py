# DP's 2 approach

# 1. Memoization (Top Down) :

dp = [False] * 100


def fibM(n):
    if dp[n] != False:  # if fib(n) already calculated
        return dp[n]
    if n == 0 or n == 1:
        dp[n] = n
    else:
        dp[n] = fibM(n - 1) + fibM(n - 2)
    return dp[n]


n = 6
print(fibM(n))

# Time complexity: O(N)
# Space complexity: O(N)

# ***************************************************************************


# 2. Tabulation (Bottom Up) :

def fibT(n):
    dpT = [0] * (n + 1)  # n+1, bcz 0 based index
    dpT[0] = 0
    dpT[1] = 1
    for i in range(2, n+1):
        dpT[i] = dpT[i-1] + dpT[i-2]
    return dpT[n]


n = 6
print(fibT(n))

# Time complexity: O(N)
# Space complexity: O(N)

