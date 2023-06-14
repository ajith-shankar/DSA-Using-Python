# The cost of a stock on each day is given in an array.
# Find the maximum profit that you can make by buying and selling on those days.

# Input: arr[] = {100, 180, 260, 310, 40, 535, 695}
# Output: 865
# Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210
#                        Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655
#                        Maximum Profit  = 210 + 655 = 865
# Input: arr[] = {4, 2, 2, 2, 4}
# Output: 2
# Explanation: Buy the stock on day 1 and sell it on day 4 => 4 – 2 = 2
#                        Maximum Profit  = 2


# Solution 1: Naive approach (very inefficient solution)

def max_profit(price, start, end):
    if end <= start:
        return 0

    profit = 0

    # The day at which the stock must be bought
    for i in range(start, end):
        # The day at which stock must be sold
        for j in range(i + 1, end + 1):
            # If buying the stock at ith day and selling it at jth day is profitable
            if price[j] > price[i]:
                # update the current profit
                current_profit = price[j] - price[i] + max_profit(price, 0, i - 1) + \
                                 max_profit(price, j + 1, end)
                profit = max(profit, current_profit)
    return profit


def main():
    price = [100, 180, 260, 310, 40, 535, 695]
    start = 0
    end = len(price)
    print("Solution 1: Max profit is:", max_profit(price, start, end - 1))


if __name__ == "__main__":
    main()


# Time complexity: O(n^2)
# Space complexity: O(1)

# ************************************************************************************************

# Solution 2: Using valley peak approach

def max_profit(price, days):
    profit = 0
    for i in range(1, days):
        # to check adjacent elements are in increasing order
        if price[i] > price[i-1]:
            # add difference into profit
            profit = profit + price[i] - price[i-1]

    return profit


def main():
    price = [100, 180, 260, 310, 40, 535, 695]
    days = len(price)
    print("Solution 2: Max profit is:", max_profit(price, days))


if __name__ == "__main__":
    main()

# Time complexity: O(n)
# Space complexity: O(1)
